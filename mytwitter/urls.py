from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitter.views import mainpage,addUser,searchFollowing,postTweet,userTweets,addFollowing
import settings,os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytwitter2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^mainpage/$',mainpage),
    (r'^addUser/$', addUser),
    (r'^searchFollowing/$', searchFollowing),
    (r'^mainpage/tweet/$', postTweet),
    (r'^addFollowing/tweet/$', postTweet),
    (r'^postTweet/$', postTweet),
    (r'^userTweets/$',userTweets),
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
