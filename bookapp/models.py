from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Categories', max_length=150)
    slug = models.SlugField(max_length=150)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.CharField(max_length=150)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    try_something_new = models.BooleanField(default=False)
    top_picks_for_you = models.BooleanField(default=False)
    find_your_new_favorite_story = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_book