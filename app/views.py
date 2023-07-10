from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def studentform(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse('valid data')
        else:
            return HttpResponse('invalid data')
    return render(request,'studentform.html',d)



