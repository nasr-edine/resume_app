from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')
