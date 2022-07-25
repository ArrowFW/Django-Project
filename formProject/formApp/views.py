from django.shortcuts import render
from . import forms

# Create your views here.

def empDetailsView (request):
    form = forms.empInfoForm()
    empData = {'formData':form}
    return render(request,'formApp/index.html',context=empData)

    
