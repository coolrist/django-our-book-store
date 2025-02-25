from django.shortcuts import render
from rest_framework.decorators import api_view
from core import utils as ut

# Create your views here.


@api_view()
def home(request):
    return render(request, 'home/index.html', {
        "meta": ut.metadata("Home page", description="Our Book Store Home page", keywords="Books, unica, creative, html", author="Sergey Pozhilov (GetTemplate.com)")   
    })
