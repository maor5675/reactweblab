from django.urls import path
from . import views

app_name = 'Data'

urlpatterns = [
   path('device/', views.Devicedata, name="devicedata"),
]