from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=250)
	body = models.TextField(blank=True)
	created_at = models.DateTimeField(default=datetime.now,blank=True)	
