from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models.fields import return_None
from django.shortcuts import render
from django.template.context_processors import request

from .models import Category, Photo
# from .models import PhotoForm, Photo

from unicodedata import category

def index(request):
    c = Category.objects.all()
    return render(request, 'tour/index.html', {"category": c})

def category_gallery(request, category_id):
    category = Category.objects.get(id=category_id)
    photos = Photo.objects.filter(category=category)
    return render(request,
                  'tour/contest-details.html',
                  {'category': category,
                'photos':photos})
def category_list(request):
    category = Category.objects.all()
    return render(request, 'tour/categories.html',  {"category": category})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Photo
from .forms import PhotoForm

def category_gallery(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    photos = Photo.objects.filter(category=category)
    form = PhotoForm()
    return render(request, 'tour/contest-details.html', {
        'category': category,
        'photos': photos,
        'form': form
    })

def add_photo_to_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.category = category
            new_photo.save()
    return redirect('category_gallery', category_id=category_id)


def add_photo_to_category(request, category_id):
    category = get_object_or_404('Category, id=category_id')
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo_category = category
            new_photo.author = request.user.username
            new_photo.save()
    return redirect('category_gallery',
                    category_id=category_id)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm
    return render(request,
                'tour/signup.html',
                {'form': form})


