from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('<a href="https://www.cannybits.com">Welcome to Canny Bits</a>')

def index(request):
    hmpage = {'homepage_insert':'HOME PAGE'}
    return render(request, 'fadmad/homepage.html',context=hmpage)


def contact(request):
    contdict = {'contact_insert':'CONTACT PAGE'}
    return render(request, 'fadmad/contact.html',context=contdict)