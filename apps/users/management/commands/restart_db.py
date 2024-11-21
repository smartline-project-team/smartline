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
                    if migrations_dir.exists() and migrations_dir.is_dir():
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

        self.stdout.write("Создаём суперпользователя...")
        os.system('echo "from django.contrib.auth import get_user_model; '
                  'User = get_user_model(); '
                  'User.objects.create_superuser(\'admin@admin.com\', \'admin\')" | python manage.py shell')

        self.stdout.write(self.style.SUCCESS("База данных успешно перезапущена, суперпользователь создан."))
