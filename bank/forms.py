from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Transactions
from django.contrib.auth.forms import User


class GetuserAccountMixin():
    def get_user_account(self, acc_no):
        try:
            return MyUser.objects.get(account_number=acc_no)
        except:
            return None


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["first_name", "username", "email", "password1", "password2", "account_number",
                  "account_type", "balance", "phone_number"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "account_number": forms.TextInput(attrs={"class": "form-control"}),
            "balance": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput({"placeholder": "Enter username"}))
    password = forms.CharField(widget=forms.PasswordInput({"placeholder": " Enter your password"}))


class TransactionForm(forms.Form, GetuserAccountMixin):
    from_account_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"class": "form-control"}))
    to_account_number = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_account_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"class": "form-control"}))
    Amount = forms.FloatField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    Note = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))


    def clean(self):
        cleaned_data = super().clean()
        from_account_number = cleaned_data.get("from_account_number")
        to_account_number = cleaned_data.get("to_account_number")
        confirm_account_number = cleaned_data.get("confirm_account_number")
        Amount = cleaned_data.get("Amount")
        Note = cleaned_data.get("Note")
        if to_account_number != confirm_account_number:
            msg = "account number mismatch"
            self.add_error('confirm_account_number', msg)
        user = GetuserAccountMixin()
        account = user.get_user_account(confirm_account_number)
        if not account:
            msg = "invalid account number"
            self.add_error('confirm_account_number', msg)
        account = user.get_user_account(from_account_number)
        if account.balance < Amount:
            msg = "Insufficient balance"
            self.add_error('Amount', msg)
