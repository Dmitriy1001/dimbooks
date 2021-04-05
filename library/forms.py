from django import forms
from django.core.exceptions import ValidationError
from .models import Book, Author

# Book

class BookAddForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'slug', 'image', 'annotation', 'text', 'author')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
			'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Слаг'}),
			'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка на изображение'}),
			'annotation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Аннотация'}),
			'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'add':
			raise ValidationError('Слаг не может называться "add"')
		if Book.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError(f'Ошибка уникальности, такой слаг уже существует')
		return new_slug	

class BookEditForm(BookAddForm):
	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		return new_slug

# Author

class AuthorEditForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('name', 'slug', 'image', 'about')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ф.И.О'}),
			'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Слаг'}),
			'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка на изображение'}),
			'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Про автора'}),
		}		