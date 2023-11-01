from django.contrib import admin
from django.urls import path
from app.views import homePage, details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    path('findDetails/<int:projectNum>', details, name='findDetails')
]
  