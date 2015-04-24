from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from twitter.models import User,Tweet,Following
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.db.models import Count,Q
from .forms import LoginForm,CreateAccount
import json as simplejson

#Search Following
@csrf_exempt
def searchfollowing(request):
	request_context = RequestContext(request)
	username=request.POST.get('tweetField')
	contents=[]
	list1=[]
	if Tweet.objects.filter(userName=username).count()!=0:
		contents=Tweet.objects.all().filter(userName=username).values_list('content',flat=True)
		for item in contents:
			list1.append(item)
		json_list=simplejson.dumps(list1)

		return render_to_response('singleTwitter.html',{'username':username,'keys':json_list})

	return render_to_response('singleTwitter2.html',{'username':username})

# Create your views here.
def mainPage(request):
	form1=LoginForm(request.POST)
	form2=CreateAccount(request.POST)
	return render_to_response('mainPage2.html',{'form1':form1,'form2':form2})

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

#user page
@csrf_exempt
def login(request):
	ct1=0
	ct2=0
	list1=[]
	request_context = RequestContext(request)
	followers=[]
	follower_contents=[]

	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			passwd=form.cleaned_data['passwd']

			if User.objects.filter(userName=username):
				if User.objects.filter(passwd=passwd):
					contents=User.objects.all().filter(~Q(userName=username)).values_list('userName',flat=True)
				
					for item in contents:
						if Following.objects.filter(userName=username).filter(following=item).count()==0:
							list1.append(item)

					u1=Following.objects.filter(userName=username).values_list('following',flat=True)
					for un in u1:
						ct2=ct2+1
						c1=Tweet.objects.all().filter(userName=un).values_list('content',flat=True)
						for ct in c1:
							followers.append(un)
							follower_contents.append(ct)
					user_list=simplejson.dumps(followers)
					content_list=simplejson.dumps(follower_contents)
					json_list=simplejson.dumps(list1)


					for ct in Tweet.objects.filter(userName=username):
						ct1=ct1+1
					

					

					return render_to_response('userpage.html',{'user':username,'passwd':passwd,'ct':ct1,'keys':json_list,'userlist':user_list,'contentlist':content_list,'ct2':ct2})
			
	form1=LoginForm()
	form2=CreateAccount()	
	return render(request,'mainPage2.html',{'form1':form1,'form2':form2})

@csrf_exempt
def addUser(request):
	request_context = RequestContext(request)

	if request.method=='POST':
		form=CreateAccount(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			email=form.cleaned_data['email']
			passwd=form.cleaned_data['passwd']
			p1=User(userName=username,nikename=email,passwd=passwd)
			p1.save()

	form1=LoginForm()
	form2=CreateAccount()

	return render_to_response('mainPage2.html',{'form1':form1,'form2':form2})

@csrf_exempt
def postTweet(request):
	request_context = RequestContext(request)

	if request.method=='POST':
		username=request.POST['username']
		text=request.POST['textArea']
		p=Tweet(userName=username,content=text)
		p.save()

	return render_to_response('submit.html')

# add Following
@csrf_exempt
def addFollowing(request):
	request_context = RequestContext(request)

	ct1=0
	ct2=0
	list1=[]
	followers=[]
	follower_contents=[]
	if request.method=='POST':
		username=request.POST['username']
		followname=request.POST['followname']

		if Following.objects.filter(userName=username).filter(following=followname).count()==0:
			p=Following(userName=username, following=followname)
			p.save()

		contents=User.objects.all().filter(~Q(userName=username)).values_list('userName',flat=True)
				
		for item in contents:
			if Following.objects.filter(userName=username).filter(following=item).count()==0:
				list1.append(item)
		json_list=simplejson.dumps(list1)

		u1=Following.objects.filter(userName=username).values_list('following',flat=True)
		for un in u1:
			ct2=ct2+1
			c1=Tweet.objects.all().filter(userName=un).values_list('content',flat=True)
			for ct in c1:
				followers.append(un)
				follower_contents.append(ct)
		user_list=simplejson.dumps(followers)
		content_list=simplejson.dumps(follower_contents)

		for ct in Tweet.objects.filter(userName=username):
			ct1=ct1+1

		return render_to_response("userpage.html",{'user':username,'ct':ct1,'ct2':ct2,'keys':json_list,'userlist':user_list,'contentlist':content_list});