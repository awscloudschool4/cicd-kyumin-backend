"""
URL configuration for awswiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, register_converter
from .converters import DateConverter  # Adjust this import according to where your converters.py is located
register_converter(DateConverter, 'date')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job/', include('job.urls')),
    path('note/', include('note.urls')),
    path('photo/', include('photo.urls')),
]