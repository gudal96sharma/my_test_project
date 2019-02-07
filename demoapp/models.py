from __future__ import unicode_literals



# Create your models here.
from django.db import models

class Category(models.Model):

    category = models.CharField(max_length=64)

    def __str__(self):
        return "%s" % (self.category)


class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)


    def __str__(self):
        return "%s" % (self.name)

class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    model_pic = models.ImageField(upload_to = 'demoapp/templates/pic_folder', blank=True)
    body = models.TextField()


    def __str__(self):
        return "%s" % (self.title)
