from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=100)