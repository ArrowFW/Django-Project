from django.shortcuts import render
import datetime
# Create your views here.
def welcome(request):
    date = datetime.datetime.now()
    date_dict = {'display_date':date}
    return render(request,'sampleApp/index.html',context=date_dict)

