from django import forms

from user.models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'sex', 'birthday', "location"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_max_distance(self):
        cleaned = super().clean()
        if cleaned['max_distance'] < cleaned['min_distance']:
            raise forms.ValidationError('max_ditance 必须大于 min_ditance')
        else:
            return cleaned['max_distance']

    def clean_max_dating_age(self):
        cleaned = super().clean()
        if cleaned['max_dating_age'] < cleaned['min_dating_age']:
            raise forms.ValidationError('max_dating_age 必须大于 min_dating_age')
        else:
            return cleaned['max_dating_age']
