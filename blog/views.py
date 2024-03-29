from django.shortcuts import render
from django.utils import timezone
from .models import Post



# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'strposts1': posts,
        'strposts2': posts,
        'strposts3': posts,
    }
    return render(request, 'blog/post_list.html', context)

	
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')