from django.shortcuts import render

from ..model.flatform import FlatFrom


def flat_form_list(request):
    flat_from_list = FlatFrom.objects.all()
    return render(request, 'flatformlist.html', {
        'flat_form_list': flat_from_list
    })