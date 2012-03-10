# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from component.models import *
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse

def supplier(request, sup_id):
	
	return HttpResponse('Suppliers:')

def suppliers(request):
	suppliers = Supplier.objects.all()
	items = len(suppliers) > 0
	return render_to_response('component/suppliers.html', 
		{	'suppliers':suppliers,
			'items':items,
		})