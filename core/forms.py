from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(required=True)
    your_email = forms.EmailField(required=True)

    your_message = forms.CharField(widget=forms.Textarea, required=True)

