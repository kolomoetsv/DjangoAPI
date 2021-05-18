from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):

    BOOK_GENRES = (
        ('action_adventure', 'Action and Adventure'),
        ('detective', 'Detective'),
        ('fantasy', 'Fantasy'),
        ('hist_fic', 'Historical Fiction'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci_fi', 'Sci-Fi'),
    )

    title = models.CharField(max_length=200, verbose_name='Book title')
    author = models.CharField(max_length=200, verbose_name='Author of the book')
    genre = models.CharField(max_length=20, choices=BOOK_GENRES, help_text='Select a genre for this book')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Authors name')
    last_name = models.CharField(max_length=100, verbose_name='Authors surname')
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0},{1}'.format(self.last_name, self.first_name)