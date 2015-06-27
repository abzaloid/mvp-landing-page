# coding=utf-8

from django import forms

from .models import SignUp

from django.utils.translation import ugettext as _

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)
	def __init__(self, *a, **kw):
		super(ContactForm, self).__init__(*a, **kw)
		self.fields['full_name'].label = u"Полное имя"
		self.fields['message'].label = u"Сообщение"


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
	def __init__(self, *a, **kw):
		super(SignUpForm, self).__init__(*a, **kw)
		self.fields['full_name'].label = u"Полное имя"

	def clean_email(self):
		# email = self.cleaned_data.get('email')
		# email_base, provider = email.split('@')
		# domain, extension = provider.split('.')
		# if not extension == 'edu':
		# 	raise forms.ValidationError("Please use a valid college email address.")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		if len(full_name) == 0:
			raise forms.ValidationError(u"Пожалуйста, введите полное имя.")
		return full_name
