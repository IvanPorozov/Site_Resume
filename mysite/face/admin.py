from django.contrib import admin
from .models import ShortenedLink, Comment, Resume, Headers

admin.site.register(ShortenedLink)
admin.site.register(Comment)
admin.site.register(Resume)
admin.site.register(Headers)
