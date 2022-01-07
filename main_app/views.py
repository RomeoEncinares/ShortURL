from django.shortcuts import render
from .forms import LinkForm
import pyshorteners

def index(request):
    form = LinkForm(request.POST or None)
    shorturl = ""

    if form.is_valid():
        url = request.POST['url']
        shorturl = create(url)

    context = {
        "form" : form,
        "shorturl": shorturl,
    }

    return render(request, 'index.html', context)

def create(url):
    shorturl = pyshorteners.Shortener().tinyurl.short(url)
    return shorturl