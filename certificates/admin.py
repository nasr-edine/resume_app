from django.contrib import admin
from .models import Certificate
from django.contrib.auth.admin import UserAdmin


@admin.register(Certificate)
class CertificateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')
