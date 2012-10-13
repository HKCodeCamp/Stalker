from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseServerError
from stalkerapp.forms import LoginForm
from stalkerapp.models import Stalker, Spotting, Subscription, Celebrity
from django.utils import simplejson
import logging
from django.template.context import RequestContext
from google.appengine.ext import db

FETCH_LIMIT = 10000

# Inserts some data into the database for testing purposes.
def build_test_view(request):
    stalker = Stalker(email='test@test.com', password='123')
    stalker.put()
    
    celebrity1 = Celebrity(name='Jackie Chan')
    celebrity1.put()
    
    celebrity2 = Celebrity(name='Angelina Jolie')
    celebrity2.put()
    
    subscription = Subscription(stalker=stalker.key(), celebrity=celebrity1.key())
    subscription.put()
    
    spotting1 = Spotting(celebrity=celebrity1.key(), stalker=stalker.key(), location='abcdefghj', comment='Comment1')
    spotting1.put()
    
    spotting2 = Spotting(celebrity=celebrity1.key(), stalker=stalker.key(), location='klmopqrst', comment='Comment2')
    spotting2.put()
    
    return HttpResponseServerError()

# Returns the key for a given email and password, status:fail otherwise
def login_view(request):
    result = ''

    if request.method == 'POST':
        json_data = simplejson.loads(request.raw_post_data)
        username = json_data['username']
        password = json_data['password']
        if (username == None) or (password == None):
            return HttpResponseServerError()
        else:
            stalkers = Stalker.all().filter('email', username).filter('password', password).fetch(1)
            if len(stalkers) == 1:
                #stalker_id = stalkers[0].key().id()
                stalker_id = str(stalkers[0].key())
                result = {'user_id':stalker_id}
            else:
                result = {'status':'fail'}
                return HttpResponseServerError(simplejson.dumps(result), mimetype="text/json")
                

        return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Registers a new stalker with the system. All requests must be submitted via POST (returns Http 500 otherwise).
# Returns status:fail if the email is already taken,  status:success otherwise.
def register_view(request):
    result = ''

    if request.method == 'POST':
        json_data = simplejson.loads(request.raw_post_data)
        s_username = json_data['username']
        s_password = json_data['password']
        if (s_username == None) or (s_password == None):
            result = {'status':'fail'}
            return HttpResponseServerError(simplejson.dumps(result), mimetype="text/json")    
        else:
            stalkers = Stalker.all().filter('email', s_username).fetch(1)
            if len(stalkers) == 0:
                stalker = Stalker(email=s_username, password=s_password)
                stalker.put()
                result = {'user_id':str(stalker.key()), 'username':stalker.email}
                return HttpResponse(simplejson.dumps(result), mimetype="text/json")
            else:
                result = {'status':'failure', 'reason': 'Email is already taken.'}
                return HttpResponseServerError(simplejson.dumps(result), mimetype="text/json")        
    else:
        return HttpResponseServerError()

# Returns the profile for a given key
def profile_view(request, userid):
    result = ''
    
    # See also http://stackoverflow.com/questions/5824801/serialize-an-entity-key-to-a-string-in-python-for-gae
    # stalker_key = db.Key.from_path('Stalker', '2')
    # stalker = db.get(stalker_key)

    stalker_key = db.Key(userid)
    # stalker = db.get(stalker_key)
    
    subscriptions_list = []
    subscriptions = Subscription.all().filter('stalker', stalker_key).fetch(FETCH_LIMIT)
    for subscription in subscriptions:
        subscriptions_list.append({'celebrity_id':str(subscription.celebrity.key()), 'name':subscription.celebrity.name})
    
    spottings_list = []
    spottings = Spotting.all().filter('stalker', stalker_key).fetch(FETCH_LIMIT)
    for spotting in spottings:
        date_string = spotting.date.strftime("%Y-%m-%dT%H-%M-%S")
        spottings_list.append({'spotting_id':str(spotting.key()), 'celebrity_id': str(spotting.celebrity.key()), 'celebrity_name': spotting.celebrity.name, 'location':spotting.location, 'comment':spotting.comment, 'date':date_string})
    
    subscriptions_json = simplejson.dumps(subscriptions_list)
    spottings_json = simplejson.dumps(spottings_list)
    
    result = {'spottings_count': len(subscriptions), 'following_count': len(spottings), 'celebrities': subscriptions_json, 'spottings': spottings_json}

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Returns a list of Celebrities matching "Name%".
# If none are found, returns celebrity:''.
def search_view(request, name):
    result = []
    
    search_result = db.GqlQuery("SELECT * FROM Celebrity WHERE name >= :1 AND name < :2", name, name + u"\ufffd").fetch(25)
    
    if len(search_result) == 0:
        result = {'celebrity':''}
    else:
        for celebrity in search_result:
            result.appen({'celebrity_id':str(celebrity.key()), 'celebrity_name':celebrity.name})

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Creates a new subscription for a given user key and celebrity key.
# Returns the subscription key if successful.
def follow_view(request):
    result = ''
    
    json_data = simplejson.loads(request.raw_post_data)
    stalker_id = json_data['username']
    celebrity_id = json_data['celebrity_id']
    
    celebrity_key = db.Key(celebrity_id)
    stalker_key = db.Key(stalker_id)
    subscription = Subscription(celebrity=celebrity_key, stalker=stalker_key)
    subscription.put()
    result = {'subscription_id':str(subscription.key())}

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Removes an existing subscription with a given user key and celebrity key.
# Returns status:failure if that subscription didn't exist, status:success if un-subscription succeeded.
def unfollow_view(request):
    result = ''
    
    json_data = simplejson.loads(request.raw_post_data)
    stalker_id = json_data['username']
    celebrity_id = json_data['celebrity_id']
    
    celebrity_key = db.Key(celebrity_id)
    stalker_key = db.Key(stalker_id)
    subscription = Subscription.all().filter('celebrity', celebrity_key).filter('stalker', stalker_key).fetch(1)
    if len(subscription) == 1:
        subscription[0].delete()
        result = {'status':'success'}
    else:
        result = {'status':'failure'}

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Returns a list of all the spottings for the celebrities a user is following.
def personal_list_view(request, userid):
    result = [] #Ask
    
    stalker_key = db.Key(userid)
    subscriptions = Subscription.all().filter('stalker', stalker_key).fetch(FETCH_LIMIT)
    for subscription in subscriptions:
        spottings = Spotting.all().filter('celebrity',subscription.celebrity.key()).order('-date').fetch(25)
        for spotting in spottings:
            date_string = spotting.date.strftime("%Y-%m-%dT%H-%M-%S")
            result.append({'spotting_id':str(spotting.key()), 'celebrity_id': str(spotting.celebrity.key()), 'celebrity_name': spotting.celebrity.name, 'location':spotting.location, 'comment':spotting.comment, 'date':date_string})    

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Returns a list of the latest spottings. 
def global_list_view(request):
    result = []

    spottings = Spotting.all().order('-date').fetch(25)
    for spotting in spottings:
        result.append({'spottingid':str(spotting.key()), 'celebrityid':str(spotting.celebrity.key()), 'celebrityname':spotting.celebrity.name, 'location':spotting.location, 'comment':spotting.comment})    
    
    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Returns the details and a list of the last 5 spottings for a given celebrity key. 
def detail_view(request, celebrityid, userid):
    result = ''

    stalker_key = db.Key(userid)
    celebrity_key = db.Key(celebrityid)
    
    subscribed_string = 'false'
    subscribed = Subscription.all().filter('stalker', stalker_key).filter('celebrity', celebrity_key).fetch(1)
    if len(subscribed) > 0:
        subscribed_string = 'true'
    
    spottings_list = []
    last_spottings = Spotting.all().filter('celebrity',celebrity_key).order('-date').fetch(5)
    for spotting in last_spottings:
        date_string = spotting.date.strftime("%Y-%m-%dT%H-%M-%S")
        spottings_list.append({'spotting_id':str(spotting.key()), 'celebrity_id': str(spotting.celebrity.key()), 'celebrity_name': spotting.celebrity.name, 'location':spotting.location, 'comment':spotting.comment, 'date':date_string})
    
    spottings_json = simplejson.dumps(spottings_list)
    
    result = {'celebrity_id':str(spotting.celebrity.key()), 'celebrity_name':spotting.celebrity.name, 'following': subscribed_string, 'spottings':spottings_json}

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")


def spotting_view(request):
    result = ''
    
    if request.method == 'POST':
        json_data = simplejson.loads(request.raw_post_data)
        s_celebrity_key = json_data['celebrity_id']
        s_celebrity_name = json_data['celebrity_name']
        s_location_id = json_data['location_4sqid']
        s_location_name = json_data['location_name']
        s_comment = json_data['comment']
        s_stalker_key = json_data['userid']
        
        if s_celebrity_key is None:
            new_celebrity = Celebrity(name=s_celebrity_name)
            new_celebrity.put()
            new_spotting = Spotting(celebrity=new_celebrity.key(), stalker=db.Key(s_stalker_key), location=s_location_id, location_name=s_location_name, comment=s_comment)
            new_spotting.put()
            result = {'spotting':str(new_spotting.key())}
        else:    
            new_spotting = Spotting(celebrity=db.Key(s_celebrity_key), stalker=db.Key(s_stalker_key), location=s_location_id, location_name=s_location_name, comment=s_comment)
            new_spotting.put()
            result = {'spotting':str(new_spotting.key())}

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def mainpage(request):
    return render_to_response('index.html')
