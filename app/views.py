from django.shortcuts import render, get_object_or_404
from .models import Category,News

# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request,'news/news_list.html',context=context)

def news_detail(request,id):
    news=get_object_or_404(News,id=id,status=News.Status.Published)
    context = {
        'news':news
    }
    return render(request,'news/news_detail.html',context=context)

def home_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request,'news/news_list.html',context=context)

def uzb_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request,'news/uzb.html',context=context)

def jahon_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request,'news/jahon.html',context=context)

def sport_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request,'news/sport.html',context=context)

def fan_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request,'news/fan.html',context=context)