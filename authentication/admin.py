from django.contrib import admin

from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser')
    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
        'is_staff',
        'is_superuser',
    ]
