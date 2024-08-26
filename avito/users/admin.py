from django.contrib import admin

from users.models import UserCustomModel


@admin.register(UserCustomModel)
class UserCustomModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('id', 'username', 'email', 'first_name', 'last_name')
