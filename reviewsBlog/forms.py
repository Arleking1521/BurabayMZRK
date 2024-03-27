from django import forms
from .models import Reviews, Answer

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['author', 'IIN', 'review']
    

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']