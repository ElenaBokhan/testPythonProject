from django.shortcuts import render
from .models import Articles


def news(request):
    # get all list
    news = Articles.objects.all()

    # get nesessery amount (as example - 1)
    # news = Articles.objects.all()[:1]

    # sorted list by pointed param
    # news = Articles.objects.order_by('date')
    return render(request, 'news/index.html', {'news': news})


