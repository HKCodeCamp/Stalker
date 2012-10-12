from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from stalkerapp.forms import LoginForm
from stalkerapp.models import Stalker
from django.utils import simplejson
import logging
from django.template.context import RequestContext

def login_view(request, email, password):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def register_view(request, s_email, s_password):
    result = []
    if request.method == 'GET':
        logging.info('getted')
        if (s_email == None) or (s_password == None):
            result.append({'status':'fail'})    
        else:
            stalkers = Stalker.all().filter('email', s_email).fetch(1)
            if len(stalkers) == 0:
                stalker = Stalker(email='someemail', password='password')
                stalker.put()
                result.append({'status':'success'})
            else:
                result.append({'status':'fail'})
        return HttpResponse(simplejson.dumps(result), mimetype="text/json")
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def profile_view(request):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def search_view(request, name):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def follow_view(reques, celebrityid, userid):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def unfollow_view(request, celebrityid, userid):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def personal_list_view(request, userid):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def global_list_view(request):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def detail_view(request, celebrityid):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def spotting_view(request, celebrityid, location, comment, userid):
    result = []
    result.append({'status':'success'})
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def mainpage(request):
    return render_to_response('index.html')
