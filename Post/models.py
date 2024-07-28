from django.db import models
# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from django.utils import formats
# from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    video = models.FileField(upload_to='videos/')
    code = models.CharField(max_length=1000, unique=True)
    title = models.CharField(max_length=255)
    created_date = models.DateField(max_length=255, null=True)
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    time_of = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    quality = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.title
