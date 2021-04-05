from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import View

from .models import Book, Author
from .forms import BookEditForm, AuthorEditForm, BookAddForm
from .utils import EditObject, AddObject, DeleteObject
# Create your views here.

# Book

def is_search(request):
	search = request.GET.get('search', '')
	if search:
		return Book.objects.filter(Q(title__icontains=search)|Q(annotation__icontains=search)|Q(text__icontains=search))
	else:
		return Book.objects.all()

def books_list(request):
	books = is_search(request)
	paginator = Paginator(books, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = f'?page={page.previous_page_number}'
	else:
		prev_url = ''
	if page.has_next():
		next_url = f'?page={page.next_page_number}'
	else:
		next_url = ''

	context = {
		'page': page,
		'is_paginated': is_paginated,
		'prev_url': prev_url,
		'next_url': next_url
	}
	return render(request, 'library/books_list.html', context)

def read_book(request, slug):
	book = Book.objects.get(slug=slug)
	paginator = Paginator(book.text, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	return render(request, 'library/read_book.html', {'book': book, 'page': page})

class EditBook(EditObject, View):
	model = Book
	form_model = BookEditForm
	template = 'library/edit_book.html'

class AddBook(AddObject, View):
	form_model = BookAddForm
	template = 'library/add_book.html'

class DeleteBook(DeleteObject, View):
	model = Book
	template = 'library/delete_book.html'
	redirect_url = 'books_list_url'					

# Author

def authors_list(request):
	authors = Author.objects.all()
	return render(request, 'library/authors_list.html', {'authors': authors})

def author_page(request, slug):
	author = Author.objects.get(slug=slug)
	books = author.books.all()
	paginator = Paginator(books, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = f'?page={page.previous_page_number}'
	else:
		prev_url = ''
	if page.has_next():
		next_url = f'?page={page.next_page_number}'
	else:
		next_url = ''

	context = {
		'author': author,
		'page': page,
		'is_paginated': is_paginated,
		'prev_url': prev_url,
		'next_url': next_url
	}
	return render(request, 'library/books_list.html', context)
	

class EditAuthor(EditObject, View):
	model = Author
	form_model = AuthorEditForm
	template = 'library/edit_author.html'
					