from django.urls import path
from  . import views

app_name = 'shapeformular'
urlpatterns = [
    path('', views.convert, name = 'convert'),
]

