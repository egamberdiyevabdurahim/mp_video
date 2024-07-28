# from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (UserSerializer, AccountSerializer, SimpleUserSerializer,
                          HistorySerializer, HiddenHistorySerializer, PDFHistorySerializer,
                          SavedLessonSerializer)
from .models import SimpleUser, User, Account, History, HiddenHistory, PDFHistory, SavedLesson


class UserViewSet(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AccountViewSet(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class SimpleUserViewSet(ListCreateAPIView):
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer


class SimpleUserView(RetrieveUpdateDestroyAPIView):
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer


class HistoryViewSet(ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class HistoryView(RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class HiddenHistoryViewSet(ListCreateAPIView):
    queryset = HiddenHistory.objects.all()
    serializer_class = HiddenHistorySerializer


class HiddenHistoryView(RetrieveUpdateDestroyAPIView):
    queryset = HiddenHistory.objects.all()
    serializer_class = HiddenHistorySerializer


class PDFHistoryViewSet(ListCreateAPIView):
    queryset = PDFHistory.objects.all()
    serializer_class = PDFHistorySerializer


class PDFHistoryView(RetrieveUpdateDestroyAPIView):
    queryset = PDFHistory.objects.all()
    serializer_class = PDFHistorySerializer


class SavedLessonViewSet(ListCreateAPIView):
    queryset = SavedLesson.objects.all()
    serializer_class = SavedLessonSerializer

class SavedLessonView(RetrieveUpdateDestroyAPIView):
    queryset = SavedLesson.objects.all()
    serializer_class = SavedLessonSerializer
