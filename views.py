from django.http import HttpResponse
from diango.shortcuts import redirect


def index(request):
    return HttpResponse('index')

def login(request):
    return redirect('/index')

