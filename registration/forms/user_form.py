from django.forms import ModelForm
from registration.models.user import MyUser

class UserForm(ModelForm):

    def save(self, force_insert=False, force_update=False, commit=True):
        user = super(ModelForm, self).save(commit=False)
        # do custom stuff
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = MyUser
        fields = ['email', 'password']