from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import News

# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.PUBLISHED)

    context = {
        'news_list':news_list
    }

    return render(request,'news/news_list.html',context=context)

def news_detail(request,slug):
    news = get_object_or_404(News, slug=slug,status=News.Status.PUBLISHED)
    context = {
        'news':news
    }
    return render(request,'news/news_detail.html',context=context)

def home_page(request):
    news_list = News.objects.filter(status=News.Status.PUBLISHED)
    mixin_news = News.objects.all().order_by('-publish_time')[:3]
    uzb_news_1 = News.objects.filter(category__name="Uzbekiston").order_by('-publish_time').first()
    uzb_news_2=News.objects.all().filter(category__name="Uzbekiston").order_by('-publish_time')[1]
    uzb_news_3=News.objects.all().filter(category__name="Uzbekiston").order_by('-publish_time')[2]
    uzb_news_4=News.objects.all().filter(category__name="Uzbekiston").order_by('-publish_time')[3]
    jahon_news=News.objects.all().filter(category__name="Jahon").order_by('-publish_time')[:5]
    fan_news_1=News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[0]
    fan_news_2=News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[1]
    fan_news_3=News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[2]
    fan_news_4=News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[3]
    sport_news_1 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[0]
    sport_news_2 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[1]
    sport_news_3 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[2]
    sport_news_4 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[3]
    sport_news_5 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[3]
    fan_news_5 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[4]
    fan_news_6 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[5]
    fan_news_7 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[6]
    fan_news_8 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[7]
    context = {
        'news_list':news_list,
        'mixin_news':mixin_news,
        'uzb_news_1':uzb_news_1,
        'uzb_news_2':uzb_news_2,
        'uzb_news_3':uzb_news_3,
        'uzb_news_4':uzb_news_4,
        'jahon_news':jahon_news,
        'fan_news_1':fan_news_1,
        'fan_news_2':fan_news_2,
        'fan_news_3':fan_news_3,
        'fan_news_4':fan_news_4,
        'sport_news_1': sport_news_1,
        'sport_news_2': sport_news_2,
        'sport_news_3': sport_news_3,
        'sport_news_4': sport_news_4,
        'sport_news_5': sport_news_5,
        'fan_news_5': fan_news_5,
        'fan_news_6': fan_news_6,
        'fan_news_7': fan_news_7,
        'fan_news_8': fan_news_8,

    }

    return render(request,'news/index.html',context=context)


def uzb_page(request):
    uzb_news_1 = News.objects.all().filter(category__name="Uzbekiston").order_by('-publish_time')[0]
    uzb_news_2=News.objects.all().filter(category__name="Uzbekiston").order_by('-publish_time')[1]
    uzb_news_3=News.objects.all().filter(category__name="Uzbekiston").order_by('-publish_time')[2]
    uzb_news_4=News.objects.all().filter(category__name="Uzbekiston").order_by('-publish_time')[3]

    context = {
        'uzb_news_1':uzb_news_1,
        'uzb_news_2':uzb_news_2,
        'uzb_news_3':uzb_news_3,
        'uzb_news_4':uzb_news_4,
    }

    return render(request,'news/uzb.html',context=context)

def jahon_page(request):
    jahon_news_1 = News.objects.all().filter(category__name="Jahon").order_by('-publish_time')[0]
    jahon_news_2 = News.objects.all().filter(category__name="Jahon").order_by('-publish_time')[1]
    jahon_news_3 = News.objects.all().filter(category__name="Jahon").order_by('-publish_time')[2]
    jahon_news_4 = News.objects.all().filter(category__name="Jahon").order_by('-publish_time')[3]

    context = {
        'jahon_news_1':jahon_news_1,
        'jahon_news_2':jahon_news_2,
        'jahon_news_3':jahon_news_3,
        'jahon_news_4':jahon_news_4,
    }

    return render(request,'news/jahon.html',context=context)

def sport_page(request):
    sport_news_1 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[0]
    sport_news_2 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[1]
    sport_news_3 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[2]
    sport_news_4 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[3]
    sport_news_5 = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[3]
    context = {
        'sport_news_1': sport_news_1,
        'sport_news_2': sport_news_2,
        'sport_news_3': sport_news_3,
        'sport_news_4': sport_news_4,
        'sport_news_5': sport_news_5,
    }

    return render(request,'news/sport.html',context=context)

def fan_page(request):
    fan_news_1 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[0]
    fan_news_2 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[1]
    fan_news_3 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[2]
    fan_news_4 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[3]
    fan_news_5 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[4]
    fan_news_6 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[5]
    fan_news_7 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[6]
    fan_news_8 = News.objects.all().filter(category__name="Fan-texnika").order_by('-publish_time')[7]

    context = {
        'fan_news_1': fan_news_1,
        'fan_news_2': fan_news_2,
        'fan_news_3': fan_news_3,
        'fan_news_4': fan_news_4,
        'fan_news_5': fan_news_5,
        'fan_news_6': fan_news_6,
        'fan_news_7': fan_news_7,
        'fan_news_8': fan_news_8,
    }

    return render(request,'news/fan.html',context=context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, "news/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, "news/contact.html", context)