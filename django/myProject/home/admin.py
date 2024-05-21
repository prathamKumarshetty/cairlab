
from django.contrib import admin
from .models import Contact, Faculty, Student, Publications, RU

# Register your models here.
admin.site.register(Contact)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Publications)
admin.site.register(RU)
