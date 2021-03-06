# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from component.models import *
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse

def supplier(request, sup_id):
    s = get_object_or_404(Supplier, pk=sup_id)
    return render_to_response('component/supplier.html',
    {   'supplier':s,
    })

def suppliers(request):
    suppliers = Supplier.objects.all()
    items = len(suppliers) > 0
    return render_to_response('component/suppliers.html', 
        {   'suppliers':suppliers,
            'items':items,
        })

def component(request, p_id='', p_num=''):
    if p_id != '':
        p = get_object_or_404(Component, pk=p_id)
        s = get_object_or_404(Supplier, pk=p.sup_id.pk)
    else:
        p = get_object_or_404(Component, partNum=p_num)
        s = get_object_or_404(Supplier, pk=p.sup_id.pk)
    return render_to_response('component/component.html',
    {'component':p,
    'supplier':s,
    })

def search(request, page=1):
    page = int(page)
    if request.method == 'POST':
        term = request.POST['term']
        p = []
        p = list(Component.objects.filter(desc__contains=term))
        p = p + list(Component.objects.filter(shortName__contains=term))
        p = p + list(Component.objects.filter(partNum__contains=term))
        p = list(set(p))
        
        
    else:
        p = list(Component.objects.all())
    
    prev = page - 1
    
    pf = p[20*(page-1):]
    
    if (len(pf) > 20):
        pf = pf[:20]
        next = page + 1
    else:
        next = 0
        
    
    return render_to_response('component/search.html',
    {   'results':pf,
        'count':min(len(p),20),
        'next': next,
        'prev': prev,
    }, context_instance=RequestContext(request)
    )