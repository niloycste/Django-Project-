from django.urls import path
from . import views

urlpatterns = [
    path('about',views.about_us),
    path('teacher/',views.teachers_info)
   
]
