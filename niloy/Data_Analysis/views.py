from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def data_analysis(request):
    return render(request,"Data_Analysis/data_analysis.html")
