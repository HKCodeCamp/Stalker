# models.py - Models for the Guestbook App
from google.appengine.ext import db
from datetime import datetime, date, timedelta
from symbol import for_stmt
import logging


## Classes for the Birthday App ##
class Stalker(db.Model):
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    registerdate = db.DateTimeProperty(auto_now_add=True)

class Celebrity(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
class Subscription(db.Model):
    stalker = db.ReferenceProperty(Stalker, required=True)
    celebrity = db.ReferenceProperty(Celebrity, required=True)
    date = db.DateTimeProperty(auto_now_add=True)

class Spotting(db.Model):
    celebrity = db.ReferenceProperty(Celebrity, required=True)
    stalker = db.ReferenceProperty(Stalker, required=True)
    location = db.StringProperty(required=True)
    location_name = db.StringProperty(required=False)
    comment = db.StringProperty(required=False)
    date = db.DateTimeProperty(auto_now_add=True)
