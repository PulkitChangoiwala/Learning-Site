from django import forms
from django.core import validators


#custom validators
def must_be_empty(value):
	if value:
		raise forms.ValidationError('is not empty')

class SuggestionForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	verify_mail = forms.EmailField(label = "Verify Your Mail")
	suggestion = forms.CharField(widget = forms.Textarea)
	honeypot = forms.CharField( required = False,
                                widget= forms.HiddenInput,
                                label ="Leave Empty",
                                #validators = [validators.MaxLengthValidator(0)]
								validators = [must_be_empty]
								)

    #clean method for complete form 

	def clean(self):

		cleaned_data = super().clean()
		email =cleaned_data.get('email')
		verify = cleaned_data.get('verify_mail')
		if  email != verify:
			raise forms.ValidationError( "Email Ids do not match" )
  