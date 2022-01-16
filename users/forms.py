from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Our registration form looks very ugly, so we're here to
# configure a few things


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # this is our chance to customize it and then later on when
        # we style this, we will need custom classes on our input fields
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            'first_name': "Name",
        }
