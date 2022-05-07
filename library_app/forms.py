from django import forms
from django.contrib.auth.forms import UserCreationForm
from library_app.models import Login, User, Book


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')
class UserRegister(forms.ModelForm):
    class Meta:
        model=User
        fields = ('name','email','phone_number','address')

class Book_Add(forms.ModelForm):
    class Meta:
        model=Book
        fields=('name','author','category')



