"""
URL configuration for New_site project.

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
from django.urls import path
from New_site import views as v1
from django.conf import settings
from django.conf.urls.static import static
from employees import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',v1.home),
    path('welcome/',v1.welcome),
    path('ge/',v2.gogd_ev),
    path("gm/",v2.gogd_mor),
    path('ga/',v2.gogd_af),
    path('time/',v2.time),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

