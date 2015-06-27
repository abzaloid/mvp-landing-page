# coding=utf-8

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils.translation import ugettext as _


from .forms import SignUpForm, ContactForm
from .getfiles import files
from .models import Point

def aktau(request):
	data = Point.objects.all().filter(city='aktau')
	city_name = u'Актау'
	start_point = '43.6596168,51.2468911'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def aktobe(request):
	data = Point.objects.all().filter(city='aktobe')
	city_name = u'Актобе'
	start_point = '50.2736838,57.1931074'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def astana(request):
	data = Point.objects.all().filter(city='astana')
	city_name = u'Астана'
	start_point = '51.1479457,71.4793897'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def atyrau(request):
	data = Point.objects.all().filter(city='atyrau')
	city_name = u'Атырау'
	start_point = '47.0983901,51.9388531'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def karaganda(request):
	data = Point.objects.all().filter(city='karaganda')
	city_name = u'Караганда'
	start_point = '49.8239824,73.168969'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def kokshetau(request):
	data = Point.objects.all().filter(city='kokshetau')
	city_name = u'Кокшетау'
	start_point = '53.2988931,69.4104623'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def kostanay(request):
	data = Point.objects.all().filter(city='kostanay')
	city_name = u'Костанай'
	start_point = '53.2054508,63.6218262'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def kyzylorda(request):
	data = Point.objects.all().filter(city='kyzylorda')
	city_name = u'Кызылорда'
	start_point = '44.8394402,65.5203463'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def pavlodar(request):
	data = Point.objects.all().filter(city='pavlodar')
	city_name = u'Павлодар'
	start_point = '52.3105033,76.9641947'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def petropavlovsk(request):
	data = Point.objects.all().filter(city='petropavlovsk')
	city_name = u'Петропавловск'
	start_point = '54.8747907,69.1603518'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def shymkent(request):
	data = Point.objects.all().filter(city='shymkent')
	city_name = u'Шымкент'
	start_point = '42.3418204,69.5898056'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def taldykorgan(request):
	data = Point.objects.all().filter(city='taldykorgan')
	city_name = u'Талдыкорган'
	start_point = '45.0105548,78.3898544'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def taraz(request):
	data = Point.objects.all().filter(city='taraz')
	city_name = u'Тараз'
	start_point = '42.8961332,71.3688612'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def uralsk(request):
	data = Point.objects.all().filter(city='uralsk')
	city_name = u'Уральск'
	start_point = '51.2181182,51.3865328'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def uskaman(request):
	data = Point.objects.all().filter(city='uskaman')
	city_name = u'Усть-каменогорск'
	start_point = '49.9665404,82.6061582'
	zoom = '13'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def crime(request):
	data = Point.objects.all().filter(city='all')
	city_name = 'all'
	start_point = '44.8394402,65.5203463'
	zoom = '4'
	context = {
		'data': data,
		'start_point': start_point,
		'city_name': city_name,
		'zoom': zoom,	
	}
	return render(request, "crime.html", context)

def olimpkz(request):
	return render(request, "olimpkz.html", {})

def dtp(request):
	return render(request, "home.html", {})

def home(request):
	title = u'Подписаться на обновления'
	subscribe = u'Подписаться'
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
			"title": u"Спасибо!",
		}
		print instance.email

	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	title = u'Написать'
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
		'signup': u'Отправить',
	}

	return render(request, "form.html", context)

