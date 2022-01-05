from django.shortcuts import render
from .forms import LinkForm
from .models import Link
import pyshorteners

def index(request):

    form = LinkForm

    context = {
        "form" : form, 
    }

    if request.method == "POST":
        shorturl = create(request.POST['url'])
        context["shorturl"] = shorturl
    
    return render(request, 'index.html', context)

def create(url):
    shorturl = pyshorteners.Shortener().tinyurl.short(url)
    return shorturl