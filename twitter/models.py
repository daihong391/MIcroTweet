from django.db import models

# Create your models here.
class User(models.Model):
	userName=models.CharField(max_length=30)
	passwd=models.CharField(max_length=50)
	nikename=models.CharField(max_length=30)

	def __unicode__(self):
        		return self.userName

class Tweet(models.Model):
	userName=models.CharField(max_length=30)
	content=models.CharField(max_length=50)

	def __unicode__(self):
        		return "%s: %s" % (self.userName,self.content)

class Following(models.Model):
	userName=models.CharField(max_length=30)
	following=models.CharField(max_length=30)

	def __unicode__(self):
		return "%s: %s" % (self.userName,self.following)