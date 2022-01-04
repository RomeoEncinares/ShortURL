from django.shortcuts import render
from .forms import LinkForm
from .models import Link

def index(request):

    form = LinkForm

    context = {
        "form" : form, 
    }
    return render(request, 'index.html', context)
