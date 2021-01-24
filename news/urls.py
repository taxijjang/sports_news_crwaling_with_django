from django.urls import path
from .views.flatform import flat_form_list, flat_form_category

from .views.naver import naver_wfootball, naver_baseballl, naver_basketball, naver_esports, naver_football, \
    naver_general, naver_golf, naver_volleyball, naver_wbaseball

urlpatterns = [
    path('flatformlist/', flat_form_list, name='flat_form_list'),
    path('naverwfootball/', naver_wfootball, name='naver_wfootball'),
    path('naverbaseballl/', naver_baseballl, name='naver_baseballl'),
    path('navergeneral/', naver_general, name='naver_general'),
    path('navergolf/', naver_golf, name='naver_golf'),
    path('navervolleyball/', naver_volleyball, name='naver_volleyball'),
    path('naverwbaseball/', naver_wbaseball, name='naver_wbaseball'),
    path('naverbasketball/', naver_basketball, name='naver_basketball'),
    path('naveresports/', naver_esports, name='naver_esports'),
    path('naverfootball/', naver_football, name='naver_football'),

]
