from django.http import HttpResponse, Http404, HttpResponseRedirect
from component.models import *
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse

# Create your views here.

def view_basket(request):
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        for k in basket.keys():
            val = int(request.POST['q_'  + k])
            basket[k] = val
        request.session['basket'] = basket
    basket = request.session.get('basket', {})
    return render_to_response('basket/viewbasket.html',
    {'basket':basket},
    context_instance=RequestContext(request)
    )

def add_to_basket(request, part_num):
    basket = request.session.get('basket', {})
    basket[part_num] = basket.get(part_num, 0) + 1
    request.session['basket'] = basket
    return HttpResponseRedirect('/basket/')

def remove_from_basket(request, part_num):
    basket = request.session.get('basket', {})
    if part_num in basket.keys():
        del basket[part_num]
    request.session['basket'] = basket
    return HttpResponseRedirect('/basket/')

def print_view(request):
    basket = request.session.get('basket', {})
    result = {}
    for k in basket.keys():
        part = get_object_or_404(Component, partNum=k)
        result[k] = [part.shortName, basket[k]]
    request.session['basket'] = {}
    return render_to_response('basket/printable.html',
    {'basket':result}
    )