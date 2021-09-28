from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import Vendedor

admin.site.register(Vendedor,auth_admin.UserAdmin)