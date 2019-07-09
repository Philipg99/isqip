from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from time import asctime
# Create your views here.


def message(request,loc):
	##models.Message.objects.all().delete()
	dit={'t':models.Message.objects.filter(location=loc)[::-1],'l':loc}
	if(request.method == "GET"):
		return render(request,'message.html',dit)
	x= models.Message(message= request.POST['message'],location= request.POST['loc'] ,time =asctime() )
	x.save()
	dit={'t':models.Message.objects.filter(location=loc)[::-1],'l':loc}
	return HttpResponseRedirect('/message/'+request.POST['loc'])


def direct(request):
	if request.method == "GET":
		x=request.POST["loc"]
		print(x)
	return render(request,'direct.html')