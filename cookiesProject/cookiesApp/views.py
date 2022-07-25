from django.shortcuts import render

# Create your views here.

# for cookies count

#def cookie_count_view(request):
#    count = request.COOKIES.get('count',0)
 #   totalCount = int (count) + 1
  ## response.set_cookie('count',totalCount)
    #return response


#for session count
  
def cookie_count_view(request):
    count = request.session.get('count',0)
    totalCount = int (count) + 1
    request.session['count'] = totalCount
    return render (request,'cookiesApp/index.html',{'count':totalCount})



### Don't forget to migrate ###
