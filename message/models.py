from django.db import models

# Create your models here.
class Message(models.Model):
	"""docstring for message"""
	message = models.TextField()
	time = models.TextField()
	location = models.TextField()
	
		