from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_phone = forms.IntegerField()
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea())
