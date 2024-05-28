from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "date"]
        labels = {
            "username": "You username",
            "user_email": "Your email",
            "content": "Your comment"
        }