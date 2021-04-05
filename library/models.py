from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, unique=True)
	image = models.CharField(max_length=5000)
	author = models.ForeignKey('Author', on_delete=models.DO_NOTHING, related_name='books', blank=True)
	annotation = models.TextField(blank=True)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'книгу'
		verbose_name_plural = 'Книги'
		ordering = ['-pub_date']

	def __str__(self):
		return self.title


class Author(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)
	image = models.CharField(max_length=5000, blank=True)
	about = models.TextField(blank=True)

	class Meta:
		verbose_name = 'автора'
		verbose_name_plural = 'Авторы'
		ordering = ['name']

	def __str__(self):
		return self.name