from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'website')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
