from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def blogs(request):
    blogs = Blog.objects.order_by('-date')
    context = {
        'title': 'Блог',
        'blogs': blogs
    }
    return render(request, 'blog/blogs.html', context=context)


def blog(request, blog_id):
    blog_ = get_object_or_404(Blog, pk=blog_id)
    context = {
        'title': blog_.title,
        'blog': blog_
    }
    return render(request, 'blog/blog.html', context=context)