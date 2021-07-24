from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name', 'last_name']}),
        ('LogIn Information', {'fields':['username', 'password'], 'classes': ['collapse']}),
    ]

admin.site.register(User, UserAdmin)
