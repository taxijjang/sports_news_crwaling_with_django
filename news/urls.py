from django.urls import path
from .views.flatform import flat_form_list
from .views.sports_news import sports_news

urlpatterns = [
    path('', flat_form_list, name='flat_form_list'),
    path('sportsnews/<slug:flat_form>/<slug:category>/', sports_news, name='sports_news'),
]