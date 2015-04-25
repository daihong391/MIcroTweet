from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from twitter.models import User,Tweet,Following
from .forms import loginForm,addForm,tweetForm
from django.db.models import Count,Q
import json as simplejson

# Create your views here.
#login form
def mainpage(request):
	if request.method=='POST':

		#redirect to userpage.html
		form=loginForm(request.POST)
		if form.is_valid():
			ct1=0
			ct2=0
			list1=[]
			followers=[]
			follower_contents=[]
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

					return render_to_response('userpage.html',{'user':username,'ct':ct1,'keys':json_list,'userlist':user_list,'contentlist':content_list,'ct2':ct2},context_instance=RequestContext(request))

	
	form1=loginForm()
	form2=addForm()

	return render_to_response('mainpage.html',{'form1':form1,'form2':form2},context_instance=RequestContext(request))

#add user form in mainpage
def addUser(request):
	if request.method=='POST':
		form=addForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			email=form.cleaned_data['email']
			passwd=form.cleaned_data['passwd']
			p1=User(userName=username,nikename=email,passwd=passwd)
			p1.save()

	form1=loginForm()
	form2=addForm()

	return render_to_response('mainpage.html',{'form1':form1,'form2':form2},context_instance=RequestContext(request))

#userpage search box
def searchFollowing(request):
	request_context = RequestContext(request)
	username=request.POST.get('tweetField')
	contents=[]
	list1=[]
	if Tweet.objects.filter(userName=username).count()!=0:
		contents=Tweet.objects.all().filter(userName=username).values_list('content',flat=True)
		for item in contents:
			list1.append(item)
		json_list=simplejson.dumps(list1)

		return render_to_response('singleTwitter.html',{'username':username,'keys':json_list},context_instance=RequestContext(request))

	return render_to_response('singleTwitter2.html',{'username':username},context_instance=RequestContext(request))

#post tweet
def postTweet(request):

	if request.method=='POST':
		form=tweetForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			textarea=form.cleaned_data['textarea']
			p=Tweet(userName=username,content=textarea)
			p.save()
			return render_to_response('submit.html',{'user':username},context_instance=RequestContext(request))

	form=tweetForm()

	return render_to_response('newTweet.html',{'form':form},context_instance=RequestContext(request))

#show user's Tweets
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

#button for adding Following
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

		return render_to_response('userpage.html',{'user':username,'ct':ct1,'ct2':ct2,'keys':json_list,'userlist':user_list,'contentlist':content_list},context_instance=RequestContext(request));