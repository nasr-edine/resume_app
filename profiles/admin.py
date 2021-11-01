from django.contrib import admin
from .models import CustomUser
from .models import Skill
from django.contrib.auth.admin import UserAdmin


@admin.register(Skill)
class SkilllAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')


@admin.register(CustomUser)
class CustomUserModelAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'email')
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Contact', {'fields': ('email',)}),
        ('security', {'fields': ('password',)}),
        ('custom fields', {'fields': ('avatar', 'title', 'bio', 'cv')})
    )
