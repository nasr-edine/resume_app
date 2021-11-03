from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(Portfolio, PortfolioAdmin)
