from __future__ import unicode_literals
from django.db import models

class Marijuana(models.Model):
    Name = models.TextField()
    Type = models.TextField()
    ParentStrain1 = models.TextField()
    ParentStrain2 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

