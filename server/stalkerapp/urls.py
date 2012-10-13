#urls.py - URL patterns for Guestbook App
from django.conf.urls.defaults import *

from django.views.generic.simple import redirect_to

urlpatterns = patterns('stalkerapp.views',			
						(r'^search/(?P<name>\w+)/', 'search_view'),
						(r'^login/(?P<email>\w+)/(?P<password>\w+)/', 'login_view'),
						(r'^register/(?P<s_email>\w+@\w+(?:\.\w+)+)(?(1))/(?P<s_password>\w+)/', 'register_view'),			
						(r'^follow/(?P<celebrityid>\w+)/(?P<userid>\w+)/', 'follow_view'),
						(r'^unfollow/(?P<celebrityid>\w+)/(?P<userid>\w+)/', 'unfollow_view'),
						(r'^list/', 'global_list_view'),
						(r'^list/(?P<userid>\w+)/', 'personal_list_view'),
						(r'^detail/(?P<celebrityid>\w+)/', 'detail_view'),
						(r'^spotting/(?P<celebrityid>\w+)/(?P<location>\w+)/(?P<comment>\w+)/(?P<userid>\w+)/', 'spotting_view'),
						(r'^profile/(?P<userid>\w+)/', 'profile_view'),
						(r'$', 'mainpage'),
)