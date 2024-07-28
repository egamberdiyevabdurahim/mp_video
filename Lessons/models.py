from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=100)
    quality = models.PositiveIntegerField()
    tags = models.CharField(max_length=255, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='lessons')
    views = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category, related_name='lessons')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    video = models.FileField(upload_to='lessons/', null=True, blank=True)

    def __str__(self):
        return self.name
