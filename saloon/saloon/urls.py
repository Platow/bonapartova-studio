from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Администрация Bonapartova Studio"

urlpatterns = [
    path('admin/', admin.site.urls),
]

