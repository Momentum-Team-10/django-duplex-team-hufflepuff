from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


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


class Framework(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    def __repr__(self):
        return f"<Framework name={self.name}>"

    def __str__(self):
        return self.name
