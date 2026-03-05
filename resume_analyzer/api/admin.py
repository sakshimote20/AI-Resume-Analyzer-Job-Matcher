from django.contrib import admin

# Register your models here.
from .models import Job

admin.site.register(Job)

from .models import Resume

admin.site.register(Resume)