from django.shortcuts import render_to_response
from django.template import RequestContext
from HelloWorld.models import Users
from django.http import HttpResponse 
import datetime
from django.contrib import messages
from HelloWorld.forms import loginForm
from django.core import serializers

def login(request):
    
    """
    To add a user
    """
    
    if request.method == 'POST':
        
            login_form = loginForm(request.POST) # A form bound to the POST data
            if login_form.is_valid(): 
                user_name = request.POST.get("username")
                user_obj = Users(username=user_name,user_create_date=datetime.datetime.now())
                user_obj.save()
                messages.success(request,"A new user has been added successfully")
                return render_to_response('home_page.html', {"user_name":user_name},context_instance=RequestContext(request))
            else:
                login_form = loginForm(request.POST)
                print login_form.errors
    else:
        login_form = loginForm()
        
    return render_to_response('login.html',{"login_form":login_form},context_instance=RequestContext(request))


   
 
def list_users(request):
    """
    returns the users in JSON format
    """
    token = request.GET.get("token")
    print token
    if token == "user123":
        ser_obj = serializers.serialize("json", Users.objects.all())
        return HttpResponse(ser_obj,mimetype='application/json')
    else:
        return render_to_response('401.html',context_instance=RequestContext(request))
        
        

