from django.shortcuts import render

from ..model.flatform import FlatFromList

from ..model.naver import NaverCategory


def flat_form_list(request):
    print('hihi')
    flat_from_list = FlatFromList.objects.all()
    return render(request, 'flatformlist.html', {
        'flat_form_list': flat_from_list
    })


def flat_form_category(request):
    naver_category_list = NaverCategory.objects.all()
    return render(request, 'flatformlist.html', {
        'naver_category_list': naver_category_list,
    })
