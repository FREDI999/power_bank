from django.shortcuts import render, redirect

# models
from blogs.models import PostsModel, CommentariyModel, MassageModel

# Create your views here.

def posts(request):
    blog = PostsModel.objects.all()
    context = {
        'blogs': blog
    }
    return render(request, template_name='blog.html', context=context)

def details(request, pk):
    detail = PostsModel.objects.get(pk=pk)
    context = {
        'detail': detail
    }
    return render(request, template_name='blog-details.html', context=context)


def commentary(request):
    if request.method == 'POST':
        l = request.POST
        name = l.get('name')
        email = l.get('email')
        phone = l.get('phone')
        commentary = l.get('commentary')
        new_object = CommentariyModel.objects.create(
            name=name,
            email=email,
            phone=phone,
            commentary=commentary
        )
        new_object.save()
    return render(request, 'blog-details.html')


def massage(request):
    if request.method == 'POST':
        l = request.POST
        name = l.get('name')
        email = l.get('email')
        commentary = l.get('commentary')
        new_object = MassageModel.objects.create(
            name=name,
            email=email,
            commentary=commentary
        )
        new_object.save()
    return render(request, 'contact.html')