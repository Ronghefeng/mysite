import re
from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("description", "document")


class AddForm(forms.Form):
    numb1 = forms.IntegerField(label="数字一")
    numb2 = forms.IntegerField(label="数字二")


def check_email(email):

    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")

    return re.match(pattern, email)


class RegistrationForm(forms.Form):

    username = forms.CharField(label="Username", max_length=50)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput
    )

    # form 中用于检查表单内容的钩子函数

    def clean_username(self):

        username = self.cleaned_data.get("username")

        if len(username) < 6:
            raise forms.ValidationError(
                "The username must contain more than 6 characters"
            )

        elif len(username) > 50:
            raise forms.ValidationError("The username is too long")

        else:

            return

    def clean_email(self):

        email = self.cleaned_data.get("email")

        if check_email(email):

            return email

        raise forms.ValidationError("Please input a valid email")

    def clean_password2(self):

        psw1 = self.cleaned_data.get("password1")
        psw2 = self.cleaned_data.get("password2")

        if psw2 != psw1:
            raise forms.ValidationError("The two passwords are different")

        return psw2


# 支持同一页面放置多个表单，extra：额外空表单数量；max_num：除空表单外的表单数量
MutilpleRegistrationForm = forms.formset_factory(RegistrationForm, extra=2, max_num=2)
 