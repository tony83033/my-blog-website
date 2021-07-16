from django.contrib import admin
from .models import myusers,myblogs

# Register your models here.

admin.site.register(myusers)
admin.site.register(myblogs)

