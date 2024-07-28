# from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Language, Lesson
from .serializers import CategorySerializer, LanguageSerializer, LessonSerializer


class CategoryViewSet(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LanguageViewSet(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageView(RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LessonViewSet(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
