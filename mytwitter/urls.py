from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitter.views import mainPage,login,addUser,newTweet,postTweet,userTweets,searchfollowing,addFollowing
import settings,os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytwitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^mainpage/$',mainPage),
    (r'^login/$', login),
    (r'^addUser/$',addUser),
    (r'^login/tweet/$',newTweet),
    (r'^postTweet/$',postTweet),
    (r'^userTweets/$',userTweets),
    (r'^searchfollowing/$',searchfollowing),
    (r'^addFollowing/$',addFollowing),
    
    (r'^css/(?P<path>.*)$','django.views.static.serve',
    	{'document_root': os.path.join(os.path.dirname(__file__),'templates/css').replace('\\','/') }
    	),
    ( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': os.path.join(os.path.dirname(__file__),'templates/css').replace('\\','/') }
    ),
    ( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': os.path.join(os.path.dirname(__file__),'templates/scripts').replace('\\','/') }
    ),

    url(r'^admin/', include(admin.site.urls)),
)
