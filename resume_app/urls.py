from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Local apps
    path('', include('profiles.urls', namespace='home')),
]
