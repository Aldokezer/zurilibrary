"""zuri_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from library import urls as library_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include(library_views.urlpatterns)),
    path('', RedirectView.as_view(url='library/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)


# This function does redirect root address to ip/library
# Allows to serve static files, like css, images etc