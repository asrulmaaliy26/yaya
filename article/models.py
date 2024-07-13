from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LPI(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    LETAK_CHOICES = [
        ('normal', 'Normal'),
        ('kiri', 'Kiri'),
        ('kanan', 'Kanan'),
        ('tengah', 'Tengah'),
    ]
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    lpi = models.ForeignKey(LPI, on_delete=models.CASCADE)
    letak = models.CharField(max_length=10, choices=LETAK_CHOICES, default='normal')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
