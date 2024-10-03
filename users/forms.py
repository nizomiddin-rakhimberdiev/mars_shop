from django.forms import ModelForm

from users.models import CustomUser


class RegisterForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'avatar', 'password')



class EditProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'avatar')