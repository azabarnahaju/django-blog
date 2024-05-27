from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True, db_index=True)     # db_index is already set to True because of the SlugField and because of the unique attribute
