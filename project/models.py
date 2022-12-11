from django.db import models
from django.forms import CharField
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, default='')
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    salt = models.CharField(max_length=1023)
    def __str__(self):
        return '%s - %s' % (self.username, self.email)
class Shelter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shelters", default='')
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=60, unique=True)
    city = models.CharField(max_length=60, default='')
    vacancies = models.IntegerField(default=0)
    additional_info = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return f'{self.name} - {self.vacancies}'
class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donations", default='')
    item = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=60, default='')
    time_range = models.CharField(max_length=60)
    condition = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.item} - {self.condition}'

class Save(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", default='')
    Shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name="shelters", default='')
    def __str__(self):
        return f'{self.user.username} - {self.Shelter.name}'
