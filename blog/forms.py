from django import forms
from .models import Contact, Sotuv, Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SotuvForm(forms.ModelForm):
    class Meta:
        model = Sotuv
        fields = '__all__'
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']