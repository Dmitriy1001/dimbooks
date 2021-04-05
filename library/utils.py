from django.shortcuts import render, redirect
from django.urls import reverse

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

			
