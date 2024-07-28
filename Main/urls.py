# """
# URL configuration for Main project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from collections import UserList

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Post.views import (CategoryList, CategoryDetail,
                        PostList, PostDetail)
from User.views import (UserViewSet, UserView,
                        SimpleUserViewSet, SimpleUserView, AccountViewSet, AccountView,
                        HistoryViewSet, HistoryView, HiddenHistoryViewSet, HiddenHistoryView,
                        PDFHistoryViewSet, PDFHistoryView, SavedLessonViewSet, SavedLessonView)
from Lessons.views import (CategoryViewSet, CategoryView, LanguageViewSet, LanguageView,
                           LessonViewSet, LessonView)
from .views import CreatePost, after_create_post, SignIn


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    # POST
    path('post/', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post'),
    path('category/', CategoryList.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_id'),
    # LESSONS
    path('lessons-lang/', LanguageViewSet.as_view(), name='language'),
    path('lessons-lang/<int:pk>/', LanguageView.as_view(), name='language_id'),
    path('lessons-category/', CategoryViewSet.as_view(), name='lessons_category'),
    path('lessons-category/<int:pk>/', CategoryView.as_view(), name='lessons_category_id'),
    path('lessons/', LessonViewSet.as_view(), name='lessons'),
    path('lessons/<int:pk>/', LessonView.as_view(), name='lessons_id'),
    # USER
    path('user/', UserViewSet.as_view(), name='user'),
    path('user/<int:pk>/', UserView.as_view(), name='user_id'),
    path('simple-user/', SimpleUserViewSet.as_view(), name='simple-user'),
    path('simple-user/<int:pk>/', SimpleUserView.as_view(), name='simple-user-id'),
    path('account/', AccountViewSet.as_view(), name='account'),
    path('account/<int:pk>/', AccountView.as_view(), name='account_id'),
    path('history/', HistoryViewSet.as_view(), name='history'),
    path('history/<int:pk>/', HistoryView.as_view(), name='history_id'),
    path('hidden_history/', HiddenHistoryViewSet.as_view(), name='hidden_history'),
    path('hidden_history/<int:pk>/', HiddenHistoryView.as_view(), name='hidden_history_id'),
    path('pdf-history/', PDFHistoryViewSet.as_view(), name='pdf-history'),
    path('pdf-history/<int:pk>/', PDFHistoryView.as_view(), name='pdf-history_id'),
    path('saved-lesson/', SavedLessonViewSet.as_view(), name='saved_lesson'),
    path('saved-lesson/<int:pk>/', SavedLessonView.as_view(), name='saved_lesson_id'),
    # MAIN
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('after_create_post/', after_create_post, name='after_create_post'),
    path('sign_in/', SignIn.as_view(), name='sign_in'),
    # SWAGGER
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
