from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import View
from .models import Book, Author
# Create your views here.

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

class EditBook(View):
	def get(self, request, slug):
		book = Book.objects.get(slug=slug)
			

def authors_list(request):
	authors = Author.objects.all()
	return render(request, 'library/authors_list.html', {'authors': authors})

def author_page(request, slug):
	author = Author.objects.get(slug=slug)
	return render(request, 'library/author_page.html', {'author': author})			