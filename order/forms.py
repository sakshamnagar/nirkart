from django.forms import ModelForm
from .models import Reviews
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('rating','review')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs = {'class': 'form-select form-control','required': 'required'}
        self.fields['review'].widget.attrs = {'class': 'form-control','rows':'5','required': 'required'}