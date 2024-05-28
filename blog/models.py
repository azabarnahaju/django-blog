from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True, db_index=True)     # db_index is already set to True because of the SlugField and because of the unique attribute

    def __str__(self):
        return f'{self.title} by {self.author}'


class Comment(models.Model):
    username = models.CharField(max_length=100)
    user_email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
