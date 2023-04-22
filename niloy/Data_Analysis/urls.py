from django.urls import path
from . import views

urlpatterns = [
    path('DA',views.data_analysis),
    
]
