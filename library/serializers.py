from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('title', 'slug', 'author', 'annotation', 'pub_date')


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('name', 'slug')		
