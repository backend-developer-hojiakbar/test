from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model):
    bio = models.TextField()
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.bio
class Products(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='products/')
    cost = models.IntegerField()
    dis_cost = models.IntegerField()
    slug = models.SlugField(max_length=300)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def __str__(self):
        return self.name
class Gallery(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='foto/')
    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    message = models.TextField()
    def __str__(self):
        return self.name
class Sotuv(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    maxsulotId = models.IntegerField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name
class Comment(models.Model):
    products = models.ForeignKey(Products,
                                 on_delete=models.CASCADE,
                                 related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"