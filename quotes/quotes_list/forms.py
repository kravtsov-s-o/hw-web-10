from django import forms
from .models import Tag, Quote, Author


class AddTag(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}))

    class Meta:
        model = Tag
        fields = ['name']


class AddAuthor(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}))
    born_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    born_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class AddQuote(forms.ModelForm):
    quote = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()
        self.fields['author'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']
