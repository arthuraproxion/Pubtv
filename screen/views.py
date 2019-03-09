from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import text_post
from .models import Movie_Post
from .models import ImagePost
from .forms import MyForm


def home(request):
    try:
        rb_index2= Movie_Post.objects.values('id')[0]['id']
    except IndexError:
        return render(request, 'screen/about.html')
    try:
        context = {
            'text': text_post.objects.all(),
            'title': 'Home',
            'video': Movie_Post.objects.get(pk=rb_index),
            'image': ImagePost.objects.all().first(),
            }
        return render(request, 'screen/home.html', context)
    except NameError:
        context = {
            'text': text_post.objects.all(),
            'title': 'Home',
            'video': Movie_Post.objects.get(pk=rb_index2),
            'image': ImagePost.objects.all().first(),}
        return render(request, 'screen/home.html', context)
    except Movie_Post.DoesNotExist:
        context = {
            'text': text_post.objects.all(),
            'title': 'Home',
            'video': Movie_Post.objects.get(pk=rb_index2),
            'image': ImagePost.objects.all().first(),}
        return render(request, 'screen/home.html', context)


def about(request):
        return render(request, 'screen/about.html', {'title': 'About'})


def videolist(request):
    global rb_index
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            rb_index = int(form.cleaned_data['List_of_Files'])
            return redirect('screen-home')
    else:
        form = MyForm()
        return render(request, 'screen/videolist.html', {'form': form, 'title': 'About'})