from django.shortcuts import render
from django.http import HttpResponse
from About_Us.models import Teacher
# Create your views here.
def about_us(request):
    return render(request,"About_us/about_us.html")


def teachers_info(request):
    teach= Teacher.objects.all()
    return render(request,"About_us/teacher.html",{'thr':teach})
