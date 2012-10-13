from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseServerError
from stalkerapp.forms import LoginForm
from stalkerapp.models import Stalker, Spotting, Subscription, Celebrity
from django.utils import simplejson
import logging
from django.template.context import RequestContext
from google.appengine.ext import db
import urllib2, urllib

FETCH_LIMIT = 10000

FOURSQUARE_CRED = 'client_id=SODCLNPZL0F0OLYWDCCGG2R0HUMHG3QTRPN0E1AVX2QU4GPP&client_secret=X4PFOW0ZIGCO5TGFPMXUGWVUXV4YC35JVIX4351FQTFZ2BVL&v=20121013'

# Inserts some data into the database for testing purposes.
def build_test_view(request):
    celebrity1 = Celebrity(name='Albert Au')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kenny Bee')
    celebrity1.put()
    celebrity1 = Celebrity(name='Danny Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Daniel Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Eason Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jackie Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jaycee Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jordan Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jason Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Sammul Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='William Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Pak Ho Chau')
    celebrity1.put()
    celebrity1 = Celebrity(name='Wakin (Emil) Chau')
    celebrity1.put()
    celebrity1 = Celebrity(name='Edison Chen')
    celebrity1.put()
    celebrity1 = Celebrity(name='Adam Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ekin Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kevin Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ronald Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Hins Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Julian Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ryan Lau')
    celebrity1.put()
    celebrity1 = Celebrity(name='Alfred Hui')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jacky Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Leslie Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Louis Koo')
    celebrity1.put()
    celebrity1 = Celebrity(name='Louis Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Steven Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Benji Chiang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Endy Chow')
    celebrity1.put()
    celebrity1 = Celebrity(name='Alex Fong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Khalil Fong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Andy Hui')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ken Hung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kelvin Kwan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kenny Kwan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Michael Kwan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Leo Ku')
    celebrity1.put()
    celebrity1 = Celebrity(name='Aaron Kwok')
    celebrity1.put()
    celebrity1 = Celebrity(name='Roger Kwok')
    celebrity1.put()
    celebrity1 = Celebrity(name='Leon Lai')
    celebrity1.put()
    celebrity1 = Celebrity(name='Bowie Lam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Chet Lam')
    celebrity1.put()
    celebrity1 = Celebrity(name='George Lam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Raymond Lam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jan Lamb')
    celebrity1.put()
    celebrity1 = Celebrity(name='Andy Lau')
    celebrity1.put()
    celebrity1 = Celebrity(name='Wilfred Lau')
    celebrity1.put()
    celebrity1 = Celebrity(name='Gene Lee')
    celebrity1.put()
    celebrity1 = Celebrity(name='Hacken Lee')
    celebrity1.put()
    celebrity1 = Celebrity(name='Edmond Leung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Tony Leung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Don Li')
    celebrity1.put()
    celebrity1 = Celebrity(name='Gallen Lo')
    celebrity1.put()
    celebrity1 = Celebrity(name='Justin Lo')
    celebrity1.put()
    celebrity1 = Celebrity(name='Lowell Lo')
    celebrity1.put()
    celebrity1 = Celebrity(name='Douglas Low')
    celebrity1.put()
    celebrity1 = Celebrity(name='Juno Mak')
    celebrity1.put()
    celebrity1 = Celebrity(name='Dennis Mak')
    celebrity1.put()
    celebrity1 = Celebrity(name='Pong Nan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Deep Ng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ron Ng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Edwin Siu')
    celebrity1.put()
    celebrity1 = Celebrity(name='William So')
    celebrity1.put()
    celebrity1 = Celebrity(name='Alan Tam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Roman Tam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Patrick Tang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Alex To')
    celebrity1.put()
    celebrity1 = Celebrity(name='Nicholas Tse')
    celebrity1.put()
    celebrity1 = Celebrity(name='Wong Cho Lam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Deric Wan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Dave Wang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Philip Wei Xiong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Chris Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Paul Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Bosco Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Anthony Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='James Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Charles Ying')
    celebrity1.put()
    celebrity1 = Celebrity(name='Shawn Yue')
    celebrity1.put()
    celebrity1 = Celebrity(name='Samuel Hui')
    celebrity1.put()
    celebrity1 = Celebrity(name='Yip Sai Wing')
    celebrity1.put()
    celebrity1 = Celebrity(name='MC Jin')
    celebrity1.put()
    celebrity1 = Celebrity(name='Bobo Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Connie Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Chelsia Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Flora Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kit Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Priscilla Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Vincy Chan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kelly Chen')
    celebrity1.put()
    celebrity1 = Celebrity(name='Joyce Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Sammi Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Stephanie Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Yumiko Cheng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Cecilia Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Teresa Cheung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Lesley Chiang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Mandy Chiang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Maggie Fu')
    celebrity1.put()
    celebrity1 = Celebrity(name='Charlene Choi')
    celebrity1.put()
    celebrity1 = Celebrity(name='Gillian Chung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Rachelle Chung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Sherman Chung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Linda Chung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Niki Chow')
    celebrity1.put()
    celebrity1 = Celebrity(name='Vivian Chow')
    celebrity1.put()
    celebrity1 = Celebrity(name='Renee Dai')
    celebrity1.put()
    celebrity1 = Celebrity(name='Theresa Fu')
    celebrity1.put()
    celebrity1 = Celebrity(name='Fiona Fung')
    celebrity1.put()
    celebrity1 = Celebrity(name='G.E.M.')
    celebrity1.put()
    celebrity1 = Celebrity(name='Cherry Ho')
    celebrity1.put()
    celebrity1 = Celebrity(name='Denise Ho')
    celebrity1.put()
    celebrity1 = Celebrity(name='Paisley Hu')
    celebrity1.put()
    celebrity1 = Celebrity(name='Deanie Ip')
    celebrity1.put()
    celebrity1 = Celebrity(name='Grace Ip')
    celebrity1.put()
    celebrity1 = Celebrity(name='Elanne Kong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ella Koon')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kellyjackie')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jade Kwan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Shirley Kwan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Susanna Kwan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Gigi Lai')
    celebrity1.put()
    celebrity1 = Celebrity(name='Vivian Lai')
    celebrity1.put()
    celebrity1 = Celebrity(name='Mag Lam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Sandy Lam')
    celebrity1.put()
    celebrity1 = Celebrity(name='Winnie Lau')
    celebrity1.put()
    celebrity1 = Celebrity(name='Coco Lee')
    celebrity1.put()
    celebrity1 = Celebrity(name='Annabelle Louie')
    celebrity1.put()
    celebrity1 = Celebrity(name='Eunix Lee')
    celebrity1.put()
    celebrity1 = Celebrity(name='Tiffany Lee')
    celebrity1.put()
    celebrity1 = Celebrity(name='Isabella Leong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Cathy Leung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Gigi Leung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Toby Leung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Rain Li')
    celebrity1.put()
    celebrity1 = Celebrity(name='Prudence Liew')
    celebrity1.put()
    celebrity1 = Celebrity(name='Candy Lo')
    celebrity1.put()
    celebrity1 = Celebrity(name='Mimi Lo')
    celebrity1.put()
    celebrity1 = Celebrity(name='Karen Morris')
    celebrity1.put()
    celebrity1 = Celebrity(name='Anita Mui')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kary Ng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Yan Ng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Cass Phang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Fiona Sit')
    celebrity1.put()
    celebrity1 = Celebrity(name='June Tang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Stephy Tang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Vangie Tang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Teresa Teng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kay Tse')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jenny Tseng')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jessica Hsuan')
    celebrity1.put()
    celebrity1 = Celebrity(name='Kate Tsui')
    celebrity1.put()
    celebrity1 = Celebrity(name='Paula Tsui')
    celebrity1.put()
    celebrity1 = Celebrity(name='Janice Vidal')
    celebrity1.put()
    celebrity1 = Celebrity(name='Jill Vidal')
    celebrity1.put()
    celebrity1 = Celebrity(name='Liza Wang')
    celebrity1.put()
    celebrity1 = Celebrity(name='Emme Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Faye Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ivana Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Linda Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='Bianca Wu')
    celebrity1.put()
    celebrity1 = Celebrity(name='Myolie Wu')
    celebrity1.put()
    celebrity1 = Celebrity(name='Sally Yeh')
    celebrity1.put()
    celebrity1 = Celebrity(name='Charlie Yeung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Miriam Yeung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Frances Yip')
    celebrity1.put()
    celebrity1 = Celebrity(name='Veronica Yip')
    celebrity1.put()
    celebrity1 = Celebrity(name='Joey Yung')
    celebrity1.put()
    celebrity1 = Celebrity(name='Ivana Wong')
    celebrity1.put()
    celebrity1 = Celebrity(name='AMA Huen Ning')
    celebrity1.put()

    
    
    stalker = Stalker(email='test@test.com', password='123')
    stalker.put()
    
    celebrity1 = Celebrity(name='Jackie Chan')
    celebrity1.put()
    
    celebrity2 = Celebrity(name='Angelina Jolie')
    celebrity2.put()
    
    subscription = Subscription(stalker=stalker.key(), celebrity=celebrity1.key())
    subscription.put()
    
    spotting1 = Spotting(celebrity=celebrity1.key(), stalker=stalker.key(), location='4fbf445de4b027be747589de', location_name='CoCoon (Coworking Space)', comment='Comment1')
    spotting1.put()
    
    spotting2 = Spotting(celebrity=celebrity1.key(), stalker=stalker.key(), location='4fbf445de4b027be747589de', location_name='CoCoon (Coworking Space)', comment='Comment2')
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
            result.append({'celebrity_id':str(celebrity.key()), 'celebrity_name':celebrity.name})

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Creates a new subscription for a given user key and celebrity key.
# Returns the subscription key if successful.
def follow_view(request):
    result = ''
    if request.method == 'POST':
        json_data = simplejson.loads(request.raw_post_data)
        stalker_id = json_data['user_id']
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
    
    if request.method == 'POST':
        json_data = simplejson.loads(request.raw_post_data)
        stalker_id = json_data['user_id']
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
            location_name = spotting.location_name
            if location_name is None:
                location_name = _resolve_location(spotting.location)
            result.append({'spotting_id':str(spotting.key()), 'celebrity_id': str(spotting.celebrity.key()), 'celebrity_name': spotting.celebrity.name, 'location':location_name, 'comment':spotting.comment, 'date':date_string})    

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

# Returns a list of the latest spottings. 
def global_list_view(request):
    result = []

    spottings = Spotting.all().order('-date').fetch(25)
    for spotting in spottings:
        date_string = spotting.date.strftime("%Y-%m-%dT%H-%M-%S")
        location_name = spotting.location_name
        if location_name is None:
            try:
                location_name = _resolve_location(spotting.location)
            except:
                location_name = 'Cocoon'
            
        result.append({'spotting_id':str(spotting.key()), 'celebrity_id':str(spotting.celebrity.key()), 'celebrity_name':spotting.celebrity.name, 'location':location_name, 'comment':spotting.comment, 'date':date_string})    
    
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
        
        if s_celebrity_key is None or len(s_celebrity_key) == 0 :
            celebrities = Celebrity.all().filter('name', s_celebrity_name).fetch(1)
            celebrity = None
            if len(celebrities) == 0:
                celebrity = Celebrity(name=s_celebrity_name)
                celebrity.put()
            else:
                celebrity = celebrities[0]

            new_spotting = Spotting(celebrity=celebrity.key(), stalker=db.Key(s_stalker_key), location=s_location_id, location_name=s_location_name, comment=s_comment)
            new_spotting.put()
            result = {'spotting':str(new_spotting.key())}
        else:    
            new_spotting = Spotting(celebrity=db.Key(s_celebrity_key), stalker=db.Key(s_stalker_key), location=s_location_id, location_name=s_location_name, comment=s_comment)
            new_spotting.put()
            result = {'spotting':str(new_spotting.key())}

    return HttpResponse(simplejson.dumps(result), mimetype="text/json")

def mainpage(request):
    return render_to_response('index.html')

def _resolve_location(location_id):
    
    file = urllib2.urlopen('https://api.foursquare.com/v2/venues/' + location_id + "?" + FOURSQUARE_CRED, None)
    try:
        response = simplejson.loads(file.read())
        venue_name = response['response']['venue']['name']
    finally:
        file.close()
    return venue_name
    
    
     