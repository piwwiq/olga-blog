from django import forms
from .models import Post

class PostForm(forms.ModelForm): #PostForm es el nom del formulari

    class Meta:
        model = Post
        fields = ("title", "text",)
