# coding=utf-8

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils.translation import ugettext as _


from .forms import SignUpForm, ContactForm

def home(request):
	title = _('Check our updates')
	subscribe = _('Subscribe')
	form = SignUpForm(request.POST or None)

	top_name = u'Статистика KZ'
	top_text = u'Вы найдете самую разную статистику Казахстана. Например, тепловую карту Казахстана с данными о криминальности и дорожно-транспортных проишевствий(ДТП) городов, правду о букмекерских конторах основанная на реальных данных и многое другое. Следите за нами.'

	context = {
		'title': title,
		'form': form,
		'subscribe': subscribe,
		'top_text': top_text,
		'top_name': top_name,
	}
	
	if form.is_valid():
		# form.save()
		instance = form.save(commit=False)
		
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Anonymous"

		instance.full_name = full_name

		instance.save()
		context = {
			"title": _("Thank You!"),
		}
		print instance.email

	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	title = _('Contact Us')
	title_align_center = True
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")
		
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'abzal.serekov@gmail.com']

		contact_message = "%s: %s via %s" %(
			form_full_name, 
			form_message, 
			form_email)

		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)

	context = {
		'form': form,
		'title': title,
		'title_align_center': title_align_center,
		'signup': _('Sign Up'),
	}

	return render(request, "form.html", context)

