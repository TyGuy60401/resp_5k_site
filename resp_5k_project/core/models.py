from django.db import models

# Create your models here.
class Feedback(models.Model):
    email = models.EmailField(max_length = 200)
    message = models.TextField()
