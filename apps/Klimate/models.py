from django.db import models

class Marijuana(models.Model):
    Name = models.TextField()
    Type = models.TextField()
    ParentStrain = models.TextFiel()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
