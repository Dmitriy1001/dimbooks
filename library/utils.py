from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

class AddObject:
	form_model, template = None, None

	def get(self, request):
		form = self.form_model()
		return render(request, self.template, {'form': form})

	def post(self, request):
		bound_form = self.form_model(request.POST)
		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)
		return render(request, self.template, {'form': bound_form})


class EditObject:
	model, form_model, template = None, None, None

	def get(self, request, slug):
		obj = self.model.objects.get(slug=slug)
		bound_form = self.form_model(instance=obj)
		return render(request, self.template, {'form': bound_form, self.model.__name__.lower(): obj})

	def post(self, request, slug):
		obj = self.model.objects.get(slug=slug)
		bound_form = self.form_model(request.POST, instance=obj)
		if bound_form.is_valid():
			edited_obj = bound_form.save()
			return redirect(edited_obj)
		return render(request, self.template, {'form': bound_form, self.model.__name__.lower(): obj})


class DeleteObject:
	model, template, redirect_url = None, None, None

	def get(self, request, slug):
		obj = self.model.objects.get(slug=slug)
		return render(request, self.template, {self.model.__name__.lower(): obj})

	def post(self, request, slug):
		obj = self.model.objects.get(slug=slug)
		obj.delete()
		return redirect(reverse(self.redirect_url))


def pagination(request, objs, objs_on_page):
	paginator = Paginator(objs, objs_on_page)
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

	return {
		'page': page,
		'is_paginated': is_paginated,
		'prev_url': prev_url,
		'next_url': next_url
	}

def what_page(model, objs_on_page, slug):
	lst = model.objects.all()
	d = {}
	page, count = 1, 0
	for i in lst:
		if count == objs_on_page:
			page += 1; count = 0
		d[i] = page; count += 1
	obj = model.objects.get(slug__iexact=slug)
	return d[obj]	
			

			
