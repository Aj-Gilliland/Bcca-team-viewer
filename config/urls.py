from django.contrib import admin
from django.urls import path
from app.views import everyoneHere, details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', everyoneHere, name='home'),
    path('findDetails/<int:teamNum>', details, name='findDetails')
]
  