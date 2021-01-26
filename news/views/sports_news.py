from django.shortcuts import render
from django.db.models import Q
from ..model.sports_news import SportsNews

def sports_news(request,flat_form, category):
    sports_news_list = SportsNews.objects.filter(
        Q(flatform=flat_form)&
        Q(category=category)
    )
    return render(request, 'sports_news.html',{
        'sports_news_list': sports_news_list,
    })