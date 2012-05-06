from django.http import HttpResponse, Http404, HttpResponseRedirect
from component.models import *
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse

# Create your views here.

def view_basket(request):
    pass

def add_to_basket(request, part_num):
    pass

def update_basket(request):
    pass