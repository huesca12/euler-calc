from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import RawRequest

# Create your views here.
def index(request):
    return HttpResponse("euler-calc terminal GUI")

def potato(request):
    return HttpResponse("potato")

class RequestView(CreateView):
    def __init__(self, model, fields):
        self.model = RawRequest
        self.fields = ('content', 'identifier')

    def post(self, request):
        # do something
        return redirect(self.model)
