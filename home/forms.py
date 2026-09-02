from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your name"
        })
    )
    

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your phone"
        })
    )

    desc = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter your message",
            "rows": 4
        })
    )