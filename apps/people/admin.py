from django.contrib import admin
from apps.people.models import Person, Credit

admin.site.register(Person)
admin.site.register(Credit)