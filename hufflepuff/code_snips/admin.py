from django.contrib import admin
from .models import User, Snippet, Language, Tag, Library, Framework, Comment
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Snippet)
admin.site.register(Language)
admin.site.register(Tag)
admin.site.register(Library)
admin.site.register(Framework)
admin.site.register(Comment)