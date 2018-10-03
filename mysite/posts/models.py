from __future__ import unicode_literals
from django.db import models
# Create your models here.

# creating a database 
class Post(models.Model):
  title       = models.CharField(max_length=120)
  description = models.TextField()
  price       = models.TextField(max_length=120)
  summary     = models.TextField(default= 'this is initial summary')
  timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

  # python 3.4
  def _unicode_(self):
    return self.title
  # python 3.6
  def __str__(self):
    return self.title