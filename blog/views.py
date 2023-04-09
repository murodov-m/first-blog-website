from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from django.views import generic

# Create your views here.


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1)
#     template_name = 'index.html'


class JokesList(generic.ListView):
    template_name = 'blog/jokes.html'

    def get_queryset(self):
        category = Category.objects.get(name='Joke')
        queryset = Post.objects.filter(status=1, category=category)
        return queryset


class PoemsList(generic.ListView):
    template_name = 'blog/poems.html'

    def get_queryset(self):
        category = Category.objects.get(name='Poem')
        queryset = Post.objects.filter(status=1, category=category)
        return queryset


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    
def home(request):
    return render(request, 'blog/index.html')


def test(request):
    message = "CONSTRUCT - Only for testing purposes"
    return render(request, 'blog/test.html', {'message': message})


def about(request):
    return render(request, 'blog/about.html')


# def jokes(request):
#     return render(request, 'blog/jokes.html')


# def poems(request):
#     return render(request, 'blog/poems.html')


def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/post_by_category.html', {'category': category, 'posts': posts})