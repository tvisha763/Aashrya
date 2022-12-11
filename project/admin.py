from django.contrib import admin
from django.contrib import admin
from .models import User, Shelter, Donation, Save
# Register your models here.

admin.site.register(User),
admin.site.register(Shelter),
admin.site.register(Donation),
admin.site.register(Save),
