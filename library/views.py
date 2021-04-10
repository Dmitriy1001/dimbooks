from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import View

from .models import Book, Author
from .forms import BookEditForm, AuthorEditForm, BookAddForm, AuthorAddForm
from .utils import EditObject, AddObject, DeleteObject, pagination, what_page
# Create your views here.

# Book

def books_list(request):
	search = request.GET.get('search', '')
	if search:
		books =  Book.objects.filter(Q(title__icontains=search)|Q(annotation__icontains=search)|Q(text__icontains=search))
	else:
		books =  Book.objects.all()
	context = pagination(request, books, 3)
	return render(request, 'library/books_list.html', context)

def read_book(request, slug):
	book = Book.objects.get(slug=slug)
	text = book.text.split('\n')
	page_n = what_page(Book, 3, slug)
	context = pagination(request, text, 50)
	context['book'] = book; context['page_n'] = page_n
	return render(request, 'library/read_book.html', context)

	
class AddBook(AddObject, View):
	form_model = BookAddForm
	template = 'library/add_book.html'

class EditBook(EditObject, View):
	model = Book
	form_model = BookEditForm
	template = 'library/edit_book.html'

class DeleteBook(DeleteObject, View):
	model = Book
	template = 'library/delete_book.html'
	redirect_url = 'books_list_url'					

# Author

def authors_list(request):
	authors = Author.objects.all()
	context = pagination(request, authors, 5)
	return render(request, 'library/authors_list.html', context)

def author_page(request, slug):
	author = Author.objects.get(slug__iexact=slug)
	books = author.books.all()
	paginator = Paginator(books, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = f'?page={page.previous_page_number()}'
	else:
		prev_url = ''
	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	context = {
		'author': author,
		'page': page,
		'is_paginated': is_paginated,
		'prev_url': prev_url,
		'next_url': next_url
	}
	return render(request, 'library/author_page.html', context)
	
class AddAuthor(AddObject, View):
	form_model = AuthorAddForm
	template = 'library/add_author.html'

class EditAuthor(EditObject, View):
	model = Author
	form_model = AuthorEditForm
	template = 'library/edit_author.html'

class DeleteAuthor(DeleteObject, View):
	model = Author
	template = 'library/delete_author.html'
	redirect_url = 'authors_list_url'	
					