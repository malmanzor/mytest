from django.db import models

# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=256)
	create_date = models.DateTimeField('Date Created')