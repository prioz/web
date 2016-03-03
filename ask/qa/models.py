from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating =  models.IntegerField()
	author = models.OneToOneField(User)
	likes = models.ManyToManyField(User)
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return '/question/%d/' % self.pk
	class Meta:
		ordering = ['-creation_date']


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.OneToOneField(Question)
	author = models.OneToOneField(User)
	likes = models.ManyToManyField(User)
	def __unicode__(self):
		return self.text
	def get_absolute_url(self):
		return '/answer/%d/' % self.pk
	class Meta:
		ordering = ['-creation_date']
