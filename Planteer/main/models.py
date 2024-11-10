from django.db import models

# Create your models here.
class Message(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    email = models.EmailField()
    message = models.TextField()
