from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from . import forms

def hello_world(request):
	return render(request,'home.html')

def suggestion_view(request):
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST) #request.POST is a dictionary
		if form.is_valid():    
			#for sendig mail set EMAIL_BACKEND in settings.py
			send_mail(

				'Suggestions from {}'.format(form.cleaned_data['name']),#subject of the mail
				form.cleaned_data['suggestion'],#body of the mail;form.cleaned_data returns a dictionary
				'<{name}  {email}>'.format(**form.cleaned_data), #email address it is frommmm
				['abc@changoiwala.com']
				)
			messages.add_message(request, messages.SUCCESS,
				'Thank For Your Suggestion')
			return HttpResponseRedirect(reverse('suggestion')) #redirects to the url corresponding to name = 'suggetion'

	return render(request,'suggestion_form.html' ,{'form' :form})