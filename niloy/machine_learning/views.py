from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    course="machine learning"
    Tclass=21
    seat=20
    cduration='2.5 months'
    offering={'c':course,'tl':Tclass,'st':seat,'cd':cduration}
    return render(request,"Machine_Learning/machine_learning.html",context=offering)


def deep_learning(request):
    Teacher={'names':['niloy','robi','asif','shuvo','nayan','mehedi']}
    return render(request,"Machine_Learning/deep_learning.html",context=Teacher)

def about_us(request):
    return render(request,"Machine_Learning/about.html")


 