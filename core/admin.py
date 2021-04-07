from django.contrib import admin
from core.models import Book


class BookAdmin(admin.ModelAdmin):
    """
    Admin view to show columns in the Django Admin for list and form view
    """
    list_display = ('id', 'author', 'title', 'description', 'poster_image')

admin.site.register(Book, BookAdmin)
