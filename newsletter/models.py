from django.db import models

class Point(models.Model):
	lat = models.FloatField()
	lng = models.FloatField()
	weight = models.FloatField()
	city = models.CharField(max_length=30)

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email


