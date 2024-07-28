from django.contrib.auth.models import AbstractUser
from django.db import models

from Lessons.models import Lesson


class User(AbstractUser):
    STATUS = (
        ('Admin', 'Admin'),
        ('Poster', 'Poster'),
        ('User', 'User'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='User')
    used = models.IntegerField(default=1)
    telegram_username = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.username


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='account')
    telegram_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)


class SimpleUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    telegram_id = models.IntegerField(unique=True, null=True)
    used = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='history')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code}/{self.user}"


class PDFHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pdf_history')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=999999999999999999999999999999999999999)
    file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return f"{self.image}/{self.user}"


class HiddenHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.text}/{self.user}"


class SavedLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lesson}/{self.user}"
