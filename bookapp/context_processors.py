from django.apps import AppConfig
from bookapp.forms import BookSearchForm

from bookapp.models import Category

class BookappConfig(AppConfig):
    name = 'bookapp'
    from .models import Category
    from .forms import BookSearchForm

def category_links(request):
    category = Category.objects.all()
    return {'categories': category}

def book_search(request):
    search_form = BookSearchForm
    if request.method == 'POST':
        search_form = BookSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return{'search_form': search_form}
