from django.contrib import admin
from .models import Book, Author
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'pub_date')
	list_filter = ('author', 'pub_date',)
	search_fields = ('title', 'text')
	date_hierarchy = 'pub_date'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	search_fields = ('name', 'about')
	