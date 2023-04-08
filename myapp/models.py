from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='uploaded images', height_field=None, width_field=None, max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    