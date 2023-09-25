from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Product, User, Lesson


# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['name', 'username', 'email', 'password1', 'password2']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['host', 'participants']

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        # exclude = ['host', 'participants']


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['avatar', 'name', 'username', 'email', 'bio']