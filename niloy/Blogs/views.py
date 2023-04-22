from django.shortcuts import render
from django.http import HttpResponse
from .forms import TeachersRegistration

# Create your views here.
def blog1(request):
    return render(request,"Blogs/blogs.html")


def showformsdata(request):
    if request.method=="POST":
        fm =TeachersRegistration(request.POST)
        if fm.is_valid():
        
         print(fm.cleaned_data['password'])
         print(fm.cleaned_data['repassword'])

         
    else:
      fm= TeachersRegistration()
      print("This is GET statement")
    # fm.order_fields(field_order=['email','first_name','last_name'])
    return render(request, 'Blogs/forms.html',{'form':fm})
     
         
         
   
   