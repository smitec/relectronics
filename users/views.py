
from django.http import HttpResponse, Http404, HttpResponseRedirect
from component.models import *
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userInfo(request):
    return "Blah"

def logout_user(request):
    logout(request)
    
    return HttpResponseRedirect('/users/login')

def login_page(request):
    error = False
    
    if request.method == 'POST':
        uname = request.POST['uname']
        pword = request.POST['pword']
        
        #attemp login and redirect
        user = authenticate(username=uname, password=pword)
        if user is not None:
            if user.is_active:
                #?? what does this return
                login(request, user)
        else:
            error = True
        
        #redirect to user profile page or some crap        
    
    print error
    return render_to_response('users/login.html',
    {'error':error}, 
    context_instance=RequestContext(request)
    )