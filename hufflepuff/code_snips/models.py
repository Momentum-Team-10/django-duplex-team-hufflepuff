from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Snippet(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    libraries = models.ManyToManyField('Library', related_name='snippets', blank=True)
    languages = models.ForeignKey('Language', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField('Tag', related_name="snippets", blank=True)
    framework = models.ForeignKey('Framework', on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"<Snippet title={self.title}>"
    
    def __str__(self):
        return self.name



class Language(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    def __repr__(self):
        return f"<Language name={self.name}>"
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    def __repr__(self):
        return f"<Tag name={self.name}>"

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length = 75)
    slug = AutoSlugField()

    def __repr__(self):
        return f"<Library name={self.name}>"

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    def __repr__(self):
        return f"<Framework name={self.name}>"

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey('User', on_delete=models.SET_NULL)
    snippet = models.ForeignKey('Snippet', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<Comment user={self.user}>"

    def __str__(self):
        return self.text
