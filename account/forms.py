from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from  account.models import Customer,Feedback





"""class BookingForm(forms.Form):
    name  = forms.CharField  (max_length = 50,
                              label      = 'Name',
                              required   = True)
    email = forms.EmailField (label      = 'E-mail',
                              required   = True)
    notes = forms.CharField  (label      = 'Notes (optional)',
                              widget     = forms.Textarea,
                              required   = False)
"""
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields="__all__"

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields="__all__"

