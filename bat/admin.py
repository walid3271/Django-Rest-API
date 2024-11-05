from django.contrib import admin
from .models import user_model

# Register your models here.
@admin.register(user_model)
class user_model_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']