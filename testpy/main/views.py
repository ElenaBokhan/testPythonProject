from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

obj = {
    "value": "main page",
    "pets": {"cat": "Vasya",
            "dog": "Sharik",
            "mouse": "Anfisa"
            }
}

dataabout = {
    "value": "about page"
}


def main(req):
    return render(req, 'main/index.html', obj)


def about(req):
    return render(req, 'main/about.html', dataabout)


def contacts(req):
    return render(req, 'main/contacts.html')
