from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Request

# Create your views here.
def index(request):
    return HttpResponse("euler-calc terminal GUI")

def potato(request):
    return HttpResponse("potato")

class RequestView(CreateView):
    model = Request
    fields = ('content', 'identifier')
