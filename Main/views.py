import threading

from django.shortcuts import render, redirect
from django.views import View

from Post.models import Category, Post


def after_create_post(request, *args, **kwargs):
    return render(request, 'after_create_post.html')


def post_video(title, video, code, language, country, time_of, genre, category_id, created_date, quality):
    Post.objects.create(
        title=title,
        video=video,
        code=code,
        language=language,
        country=country,
        time_of=time_of,
        genre=genre,
        category_id=category_id,
        created_date=created_date,
        quality=quality,
    )

class CreatePost(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'create_post.html', context)

    def post(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {'categories': categories}
        title = request.POST.get('title')
        video = request.FILES.get('video')
        code = request.POST.get('code')
        language = request.POST.get('language')
        country = request.POST.get('country')
        time_of = request.POST.get('time_of')
        genre = request.POST.get('genre')
        created_date = request.POST.get('created_date')
        quality = request.POST.get('quality')
        category_id = request.POST.get('category')
        if (title is not None and video is not None and code is not None and language is not None
            and category_id is not None and country is not None and time_of is not None
            and genre is not None and created_date is not None and quality is not None):
            threading.Thread(target=post_video, args=(title, video, code, language, country, time_of,
                                                      genre, category_id, created_date, quality)).start()
            return redirect('after_create_post')
        return render(request, 'create_post.html', context)


class SignIn(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sign_in.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username == 'mpservice' and password == '@12345aw'):
            return redirect('create_post')
        return render(request, 'sign_in.html')