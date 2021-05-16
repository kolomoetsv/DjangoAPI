from django.contrib import admin
from .models import Book, Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Years of life', {
            'fields': ('date_of_birth', 'date_of_death')
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    list_filter = ('author', 'genre')
