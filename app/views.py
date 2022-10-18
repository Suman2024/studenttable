from django.shortcuts import render
from app.models import *
# Create your views here.
def details(request):
    S=Studentdetails.objects.all()
    d={'Studentdetails':S}
    return render(request,'Studentdetails.html',d)