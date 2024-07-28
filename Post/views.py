# from django.shortcuts import render
# from django.db.models import Q, F, Count, Sum, Min, Max
# from django.utils import timezone
# from datetime import datetime, timedelta
#
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import Post, Category
from .serializers import CategorySerializer as Cat, PostSerializer as Post_s


class PostList(ListCreateAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Post.objects.all()
    serializer_class = Post_s


class PostDetail(RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Post.objects.all()
    serializer_class = Post_s


class CategoryList(ListCreateAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Category.objects.all()
    serializer_class = Cat


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Category.objects.all()
    serializer_class = Cat
