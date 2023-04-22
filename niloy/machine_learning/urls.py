from django.urls import path
from . import views

urlpatterns = [
    path('machine/',views.machine_learning),
    path('DL/',views.deep_learning),
    path('about_us/',views.about_us),
]
