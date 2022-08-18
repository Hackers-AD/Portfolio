from django.db import models


class Service(models.Model):
	icon_class = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	description = models.TextField()
	
class Portfolio(models.Model):
	cover_photo = models.ImageField(upload_to='projects')
	name = models.CharField(max_length=255)
	tagline = models.CharField(max_length=255)
	company_url = models.URLField(max_length=255, default="https://facebook.com")
	start_date = models.DateField()
	end_date = models.DateField()

class Contact(models.Model):
	email = models.EmailField()
	message = models.TextField()
	full_name = models.CharField(max_length=200, blank=True,null=True)
	created_date = models.DateTimeField(auto_now_add=True)