from django import forms
from webapp.models import Product

class RoductCreateForm(forms.ModelForm):

    name = forms.CharField(label='Наименование товара', required=True)
    category = forms.CharField(label='Категория', required=True, max_length=200)
    description = forms.Textarea()
    photo = forms.ImageField(label='Картинка', required=False)

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)

        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        user = super().save(commit=commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        profile, _ = Profile.objects.get_or_create(user=self.instance)
        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data.get(field))
        profile.avatar = self.cleaned_data.get('avatar', None)
        profile.about_me = self.cleaned_data.get('about_me', None)
        profile.github = self.cleaned_data.get('github', None)

        # self.instance.profile = profile
        if commit:
            profile.save()
