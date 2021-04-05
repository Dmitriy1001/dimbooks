from django.urls import path
from .views import *

urlpatterns = [
	path('', books_list, name='books_list_url'),
	path('book/<slug>/', read_book, name='read_book_url'),
	path('book/<slug>/edit/', EditBook.as_view(), name='edit_book_url'),
	path('authors/', authors_list, name='authors_list_url'),
	path('author/<slug>/', author_page, name='author_page_url'),
]