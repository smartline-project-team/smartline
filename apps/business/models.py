from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Specialist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='specialists_photos', blank=True, null=True)
    business = models.ForeignKey('Business', related_name='specialists', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specialist = models.ForeignKey('Specialist', related_name='services', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price} сом"

class Business(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='businesses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    specialist = models.ForeignKey(Specialist, related_name='time_slots', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_taken = models.BooleanField(default=False)

    class Meta:
        unique_together = ('specialist', 'date', 'time') 

    def __str__(self):
        status = "Taken" if self.is_taken else "Available"
        return f"{self.specialist} - {self.date} {self.time} ({status})"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time_slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user} with {self.specialist} on {self.time_slot.date} at {self.time_slot.time}"