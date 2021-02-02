import random
from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweets


# Create your views here.

def home_view(request,*args,**kwargs):
    return render(request,"pages/home.html",context={},status=200)

def home_list_view(request,*args,**kwargs):
    qs = Tweets.objects.all()
    tweet_list = [{"id":i.id,"contant":i.contant,"likes":random.randint(0,125)} for i in qs]
    data = {
        "response":tweet_list,
        "isUser":False
    }
    return JsonResponse(data)

def home_details_view(request,tweets_id,*args,**kwargs):
    data = {    
        "id":tweets_id
    }
    status=200
    try:
        obj = Tweets.objects.get(id=tweets_id)
        data['contant'] = obj.contant
    except: 
        data['message'] = 'Not Found'
        status=404
    
    return JsonResponse(data,status=status)