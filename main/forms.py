from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    contact_phone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Breif your Query'}))
