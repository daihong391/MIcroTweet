from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from twitter.models import User,Tweet
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
import json as simplejson

# Create your views here.
def mainPage(request):
	return render_to_response('mainPage2.html')

def newTweet(request):
	return render_to_response('newTweet.html')

# user tweets' page
def userTweets(request):
	mstring=[]
	for key,value in request.GET.iteritems():
		mstring.append("%s" % (value))

	# search the corresponding tweets accordingto the username
	contents=Tweet.objects.all().filter(userName=mstring[0]).values_list('content',flat=True)
	list1=[];
	for item in contents:
		list1.append(item)
	json_list=simplejson.dumps(list1)

	return render_to_response('userTweets.html',{'user':mstring[0],'keys':json_list})

@csrf_exempt
def login(request):
	username={}
	passwd={}
	ct1=0
	request_context = RequestContext(request)

	if request.method=='POST':
		username=request.POST.get('username')
		passwd=request.POST.get('passwd')

		if User.objects.filter(userName=username):
			if User.objects.filter(passwd=passwd):
				for ct in Tweet.objects.filter(userName=username):
					ct1=ct1+1
				return render_to_response('userpage.html',{'user':username,'passwd':passwd,'ct':ct1})
				
		return render(request,'mainPage2.html')

@csrf_exempt
def addUser(request):
	request_context = RequestContext(request)

	if request.method=='POST':
		fullname=request.POST['fullname']
		email=request.POST['email']
		passwd=request.POST['passwd']
		p1=User(userName=fullname,nikename=email,passwd=passwd)
		p1.save()
		
	return render_to_response('mainPage2.html')

@csrf_exempt
def postTweet(request):
	request_context = RequestContext(request)

	if request.method=='POST':
		username=request.POST['username']
		text=request.POST['textArea']
		p=Tweet(userName=username,content=text)
		p.save()

	return render_to_response('submit.html')