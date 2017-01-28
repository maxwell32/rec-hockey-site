from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from league.models import League


# Create your views here.
def index(request):
    context = {}
    return render(request, 'home/index.html')