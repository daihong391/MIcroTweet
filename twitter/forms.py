from  django import forms

class loginForm(forms.Form):
	username=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'username'}))
	passwd=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class addForm(forms.Form):
	username=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'username'}))
	email=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'email'}))
	passwd=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class tweetForm(forms.Form):
	username=forms.CharField(max_length=50, widget=forms.HiddenInput(attrs={'id':'user'}))
	textarea=forms.CharField(widget=forms.Textarea)