from django import forms


class contactform(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Number'
            }
        )
    )

    email = forms.EmailField(
        label='Emai;',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'
            }
        )
    )

    course = forms.CharField(
        label='Course',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Course'
            }
        )
    )

    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Location'
            }
        )
    )