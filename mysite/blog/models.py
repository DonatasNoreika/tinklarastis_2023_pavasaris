from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=50)
    text = HTMLField(verbose_name="Tekstas", max_length=5000)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name="Straipsnis", on_delete=models.CASCADE)
    body = models.TextField(verbose_name="Tekstas", max_length=5000)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
