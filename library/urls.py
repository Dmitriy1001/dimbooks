from django.urls import path
from .views import *

urlpatterns = [
	# book
	path('book/add/', AddBook.as_view(), name='add_book_url' ),
	path('', books_list, name='books_list_url'),
	path('book/<slug>/', read_book, name='read_book_url'),
	path('book/<slug>/edit/', EditBook.as_view(), name='edit_book_url'),
	path('book/<slug>/delete/', DeleteBook.as_view(), name='delete_book_url'),
	
	# author
	path('authors/', authors_list, name='authors_list_url'),
	path('author/<slug>/', author_page, name='author_page_url'),
	path('author/<slug>/edit/', EditAuthor.as_view(), name='edit_author_url'),
]