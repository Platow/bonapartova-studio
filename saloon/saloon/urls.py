from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

admin.site.site_header = "Администрация Bonapartova Studio"

def redirect_view(request):
    return redirect('/admin')

urlpatterns = [
    path('', redirect_view),
    path('admin/', admin.site.urls),
]

