from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
Form class for creating a user
"""
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    