from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp, Point

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp

class PointAdmin(admin.ModelAdmin):
	list_display = ["lat", "lng", "weight", "city"]
	class Meta:
		model = Point

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Point, PointAdmin)