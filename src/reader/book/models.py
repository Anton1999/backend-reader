from django.db import models
from core.models import User

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=64, verbose_name='Жанры')

	def __str__(self):
		return self.name

class Chapter(models.Model):
	chapter = models.FileField()
	count_chapter = models.IntegerField()

	

class Book(models.Model):
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
	title = models.CharField(max_length=100)
	paper_count = models.IntegerField()
	rating = models.CharField(max_length=50)
	rating_count = models.IntegerField()
	status = models.CharField(max_length=50)
	category = models.IntegerField()
	photo = models.ImageField()
	short_description = models.TextField()
	text = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Текст книги')

	def __str__(self):
		return self.title

class Rate(models.Model):
	text_rate = models.TextField()
	book = models.ForeignKey(Book, verbose_name="Rate for Book", on_delete=models.CASCADE)
	user = models.ForeignKey('core.User', verbose_name='author', on_delete=models.CASCADE)

	def __str__(self):
		return self.text_rate
