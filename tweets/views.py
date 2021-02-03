import random
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse,HttpResponseRedirect
from django.utils.http import is_safe_url
from .models import Tweets
from .forms import TweetForm


# Create your views here.
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
def home_view(request,*args,**kwargs):
    return render(request,"pages/home.html",context={},status=200)


def tweet_create_view(request,*args,**kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serializ(),status=201)
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request,'components/form.html',context={"form":form})

def home_list_view(request,*args,**kwargs):
    
    qs = Tweets.objects.all()
    tweet_list = [i.serializ() for i in qs]
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