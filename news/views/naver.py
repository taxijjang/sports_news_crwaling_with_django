from django.shortcuts import render

from ..model.naver import NaverWfootball, NaverBaseball,NaverBasketball,NaverFootball,NaverVolleyball,NaverGolf,NaverEsports,NaverGeneral,NaverWbaseball



def naver_baseballl(request):
    baseball_list = NaverBaseball.objects.all()
    return render(request, 'naver_baseball.html', {
        'baseball_list': baseball_list,
    })

def naver_basketball(request):
    basketball_list = NaverBasketball.objects.all()
    return render(request, 'naver_basketball.html', {
        'basketball_list': basketball_list,
    })

def naver_esports(request):
    esports_list = NaverEsports.objects.all()
    return render(request, 'naver_esports.html', {
        'esports_list': esports_list,
    })

def naver_football(request):
    football_list = NaverFootball.objects.all()
    return render(request, 'naver_football.html', {
        'football_list': football_list,
    })

def naver_general(request):
    general_list = NaverGeneral.objects.all()
    return render(request, 'naver_general.html', {
        'general_list': general_list,
    })

def naver_golf(request):
    golf_list = NaverGolf.objects.all()
    return render(request, 'naver_golf.html', {
        'golf_list': golf_list,
    })

def naver_volleyball(request):
    volleyball_list = NaverVolleyball.objects.all()
    return render(request, 'naver_bolleyball.html', {
        'volleyball_list': volleyball_list,
    })

def naver_wbaseball(request):
    wbaseball_list = NaverWbaseball.objects.all()
    return render(request, 'naver_wbaseball.html', {
        'wbaseball_list': wbaseball_list,
    })

def naver_wfootball(request):
    wfootball_list = NaverWfootball.objects.all()
    return render(request, 'naver_wfootball.html', {
        'wfootball_list': wfootball_list,
    })