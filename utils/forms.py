from django import forms


class BookForm(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput())
	short_name = forms.CharField(required=True, widget=forms.TextInput())
