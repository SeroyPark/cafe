from django.shortcuts import render
from django.utils import timezone
from .models import Post

def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'bake/main.html', {'posts': posts})
def pan(request):
    return render(request, 'bake/pan.html', {})
def ja(request):
    return render(request, 'bake/ja.html', {})
def yong(request):
    return render(request, 'bake/yong.html', {})
