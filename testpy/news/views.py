from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news(request):
    # get all list
    news = Articles.objects.all()

    # get nesessery amount (as example - 1)
    # news = Articles.objects.all()[:1]

    # sorted list by pointed param
    # news = Articles.objects.order_by('date')
    return render(request, 'news/index.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        error = 'form filled uncorrect'
    form = ArticlesForm()
    data = {'form': form,
            'error': error}
    return render(request, 'news/create.html', data)


