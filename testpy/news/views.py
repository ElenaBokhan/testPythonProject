from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


class DetailsShow(DetailView):
    model = Articles
    context_object_name = 'article'
    template_name = 'news/details.html'


class UpdateNews(UpdateView):
    model = Articles
    success_url = '/news'
    template_name = 'news/create.html'
    fields = ['title', 'anons', 'full_text', 'date']


class DeleteNews(DeleteView):
    model = Articles
    success_url = '/news'
    context_object_name = 'el'
    # fields = ['title', 'anons', 'full_text', 'date']
    template_name = 'news/delete.html'


def news(request):
    # get all list
    news = Articles.objects.all()

    # get nesessery amount of list (as example - 1)
    # news = Articles.objects.all()[:1]

    # sorted list by pointed param
    # news = Articles.objects.order_by('date')
    return render(request, 'news/index.html', {'news': news})


def create(request):
    err = ''
    if request.method=='POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            err = 'Форма неверно заполнена'
    form = ArticlesForm()
    data = {'form': form, 'err': err}
    return render(request, 'news/create.html', data)




