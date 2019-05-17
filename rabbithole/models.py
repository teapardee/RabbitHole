from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
	cat_name = models.CharField(max_length=250)

class SubCategory(models.Model):	
	subcat_name = models.CharField(max_length=250)

class channel(models.Model):
	cat = models.CharField(max_length=250, default="null")
	sub_cat = models.CharField(max_length=250, default="null")
	channel_name = models.CharField(max_length=250, default="null")
	uploads = models.CharField(max_length=250, default="null")	
	subscribers = models.CharField(max_length=250, default="null")
	viewcount = models.CharField(max_length=250, default="null")
	thumbnail = models.CharField(max_length=250, default="null")
	customUrl = models.CharField(max_length=250, default="null")


	def __str__(self):
		return self.channel_name

class cat_submissions(models.Model):
	cat_submission = models.CharField(max_length=200)

	def __str__(self):
		return self.cat_submission

class sub_cat_submissions(models.Model):
	sub_cat_submission = models.CharField(max_length=200)

	def __str__(self):
		return self.sub_cat_submission
