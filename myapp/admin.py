from django.contrib import admin
from . models import Book,Publisher

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')

#admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Book,BookAdmin)