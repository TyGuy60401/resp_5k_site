from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm


class U_UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First name',
            'type': 'text',
            'required': 'required',
            'autofocus': 'autofocus'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last name',
            'type': 'text',
            'required': 'required',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last name',
            'type': 'text',
            'required': 'required',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            'type': 'text',
            'required': 'required',
            'autofocus': '',
            'hx-post': '/check_username/',
            'hx-swap': 'innerHTML',
            'hx-trigger': 'keyup changed',
            'hx-target': '#username-error'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'type': 'text',
            'required': 'required',
        })
        self.fields['password2'].label = "Confirm password"
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'type': 'text',
            'required': 'required',
        })


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

class U_AuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        # super(AuthenticationForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            'type': 'text',
            'required': 'required',
            'autofocus': 'autofocus'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'type': 'text',
            'required': 'required',
        })
