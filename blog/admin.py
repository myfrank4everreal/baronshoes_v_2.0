from django.contrib import admin
from .models import Blog, Post, Author, Category,Comment


admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)

