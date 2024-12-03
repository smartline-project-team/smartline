import os
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Удаляет db.sqlite3, очищает папку media, удаляет миграции, выполняет миграции и создаёт суперпользователя.'

    def handle(self, *args, **kwargs):
        base_dir = Path(settings.BASE_DIR)

        db_path = base_dir / "db.sqlite3"
        if db_path.exists():
            self.stdout.write(f"Удаляем базу данных: {db_path}")
            db_path.unlink()
        else:
            self.stdout.write("База данных не найдена.")

        media_path = base_dir / "media"
        if media_path.exists() and media_path.is_dir():
            self.stdout.write(f"Очищаем папку media: {media_path}")
            shutil.rmtree(media_path)
            media_path.mkdir(parents=True, exist_ok=True)
        else:
            self.stdout.write("Папка media не найдена.")

        apps_dir = base_dir / "apps"
        if apps_dir.exists() and apps_dir.is_dir():
            for app in apps_dir.iterdir():
                if app.is_dir():
                    migrations_dir = app / "migrations"
                    if not migrations_dir.exists():
                        self.stdout.write(f"Создаём папку migrations в {app.name}")
                        migrations_dir.mkdir(parents=True, exist_ok=True)
                        init_file = migrations_dir / "__init__.py"
                        init_file.touch()
                        self.stdout.write(f"Создан файл {init_file}")

                    elif migrations_dir.is_dir():
                        self.stdout.write(f"Удаляем миграции в {migrations_dir}")
                        for migration_file in migrations_dir.glob("*.py"):
                            if migration_file.name != "__init__.py":
                                migration_file.unlink()
                        self.stdout.write(f"Миграции удалены в {app.name}.")
        else:
            raise CommandError("Папка apps не найдена.")

        self.stdout.write("Выполняем makemigrations и migrate...")
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")

        self.fill_db()

        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена."))
        

    def fill_db(self, *args, **kwargs):
        from apps.users.management.commands.db_data import users, categories, businesses, specialists, services, time_slots
        from django.contrib.auth import get_user_model
        from apps.business.models import Category, Business, Specialist, Service, TimeSlot

        User = get_user_model()

        User.objects.create_superuser(email='admin@admin.com',password='admin')

        for user_data in users:
            user = User.objects.create_user(**user_data)
            self.stdout.write(f"Пользователь {user.email} создан.")

        for category_data in categories:
            category = Category.objects.create(**category_data)
            self.stdout.write(f"Категория {category.name} создана.")

        for business_data in businesses:
            categories = Category.objects.filter(name__in=business_data["categories"])  # Получаем категории по их именам
            business = Business.objects.create(
                name=business_data["name"],
                description=business_data["description"],
                phone_number=business_data["phone_number"],
                email=business_data["email"],
                address=business_data["address"]
            )
            business.categories.set(categories)

        businesses_dict = {business.name: business for business in Business.objects.all()}
        specialists_dict = {}  
        for specialist_data in specialists:
            business = businesses_dict.get(specialist_data["business"])
            specialist = Specialist.objects.create(
                first_name=specialist_data["first_name"],
                last_name=specialist_data["last_name"],
                business=business
            )
            specialists_dict[f"{specialist.first_name} {specialist.last_name}"] = specialist
            self.stdout.write(f"Специалист {specialist.first_name} {specialist.last_name} создан.")

        for service_data in services:
            specialist = specialists_dict.get(service_data["specialist"])
            service = Service.objects.create(
                name=service_data["name"],
                price=service_data["price"],
                specialist=specialist
            )
            self.stdout.write(f"Услуга {service.name} создана.")

        for time_slot_data in time_slots:
            specialist = specialists_dict.get(time_slot_data["specialist"])
            time_slot = TimeSlot.objects.create(
                specialist=specialist,
                date=time_slot_data["date"],
                time=time_slot_data["time"],
                is_taken=time_slot_data["is_taken"]
            )
            self.stdout.write(f"Временной слот на {time_slot.date} {time_slot.time} для {specialist.first_name} {specialist.last_name} создан.")


        



