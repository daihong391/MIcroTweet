from django import forms

class LoginForm(forms.Form):
	username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'username','size':'15'}))
	passwd=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'password','size':'15'}))

class CreateAccount(forms.Form):
	username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'username','size':'15'}))
	email=forms.EmailField(max_length=80, widget=forms.TextInput(attrs={'placeholder':'email','size':'15'}))
	passwd=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'password','size':'15'}))