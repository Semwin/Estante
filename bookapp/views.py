from django.shortcuts import render, redirect
from .models import Book, Category
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def index(request):
    return render(request, 'bookapp/index.html')

def home(request):
    booklist = list(Book.objects.all())
    random_book = random.sample(booklist,20)
    try_something_new = random_book
    top_picks_for_you = Book.objects.filter(top_picks_for_you = True)
    find_your_new_favorite_story = Book.objects.filter(find_your_new_favorite_story = True)
    return render(request, 'bookapp/home.html', {'try_something_new': try_something_new,
    'top_picks_for_you': top_picks_for_you, 'find_your_new_favorite_story': find_your_new_favorite_story
    })

def all_books(request):
    books = Book.objects.all()
    return render(request, 'bookapp/all_books.html', {'books':books})

def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    return render(request, 'bookapp/genre_detail.html', {'category': category})

@login_required(login_url='login')
def book_detail(request, slug):
    book = Book.objects.get(slug = slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith = book_category)
    return render(request, 'bookapp/book_detail.html', {'book': book, 'similar_books': similar_books})

def search_book(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, 'bookapp/search_book.html', {'searched_books':searched_books})

def register_page(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, "Account Created Successfully!")
            return redirect('login')
           
    return render(request, 'bookapp/register.html', {'register_form': register_form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
        
    return render(request, 'bookapp/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def about_us(request):
    return render(request, 'booksite/about_us.html')