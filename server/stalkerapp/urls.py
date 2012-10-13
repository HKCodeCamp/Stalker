#urls.py - URL patterns for Guestbook App
from django.conf.urls.defaults import *

from django.views.generic.simple import redirect_to

urlpatterns = patterns('stalkerapp.views',
						(r'^buildtest/', 'build_test_view'),			
						(r'^search/(?P<name>\w+)/', 'search_view'),
						(r'^login/', 'login_view'),
						(r'^register/', 'register_view'),			
						(r'^follow/', 'follow_view'),
						(r'^unfollow/', 'unfollow_view'),
						(r'^list/', 'global_list_view'),
						(r'^list/(?P<userid>\w+(?:\-\w+)*)/', 'personal_list_view'),
						(r'^detail/(?P<celebrityid>\w+(?:\-\w+)*)/(?P<userid>\w+(?:\-\w+)*)/', 'detail_view'),
						(r'^spotting/', 'spotting_view'),
						(r'^profile/(?P<userid>\w+(?:\-\w+)+)/', 'profile_view'),
						(r'$', 'mainpage'),
)