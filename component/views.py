# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from component.models import *
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse

def supplier(request, sup_id):
	s = get_object_or_404(Supplier, pk=sup_id)
	return render_to_response('component/supplier.html',
	{	'supplier':s,
	})

def suppliers(request):
	suppliers = Supplier.objects.all()
	items = len(suppliers) > 0
	return render_to_response('component/suppliers.html', 
		{	'suppliers':suppliers,
			'items':items,
		})

def component(request, p_id):
	p = get_object_or_404(Component, pk=p_id)
	s = get_object_or_404(Supplier, pk=p.sup_id.pk)
	return render_to_response('component/component.html',
	{	'component':p,
		'supplier':s,
	})

def search(request):
	if request.method == 'POST':
		term = request.POST['term']
		p = Component.objects.get(desc__contains=term)
		return render_to_response('component/search.html',
		{	'results':p,
			'count':len(p)
		})
	else:
		p = Component.objects.all()
		return render_to_response('component/search.html',
		{	'results':p,
			'count':len(p)
		})