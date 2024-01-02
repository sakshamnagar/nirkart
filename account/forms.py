from django.forms import ModelForm
from .models import Vendor, Address
from django.contrib.auth.models import User
from order.models import Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets = {
        'username':forms.TextInput(attrs={
            'class':'form-control rounded-3',
            'id':'floatingInput',
            'required': 'required',
        }),
        'first_name':forms.TextInput(attrs={
            'class':'form-control rounded-3',
            'id':'floatingInput',
            'required': 'required',
        }),
        'last_name':forms.TextInput(attrs={
            'class':'form-control rounded-3',
            'id':'floatingInput',
            'required': 'required',
        }),
        'email':forms.TextInput(attrs={
            'class':'form-control rounded-3',
            'id':'floatingInput',
            'required': 'required',
        })}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}
        self.fields['password2'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}

class Login(AuthenticationForm):
    class Meta:
        model=User
        fields = ('username','password1')
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}
        self.fields['password'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model=User
        fields=('old_password', 'new_password1', 'new_password2')
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}
        self.fields['new_password1'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}
        self.fields['new_password2'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}



class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ('store_name','gst_number', 'pickup_address1','pickup_address2','city','state','zip_code')
        widgets = {
            'store_name': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'gst_number': forms.NumberInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'pickup_address1': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'pickup_address2': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'city': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'state': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'zip_code': forms.NumberInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
        
        }


class UpdateVendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ('store_name','gst_number', 'pickup_address1','pickup_address2','city','state','zip_code')
        widgets = {
            'store_name': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'gst_number': forms.NumberInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'pickup_address1': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'pickup_address2': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'city': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'state': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'zip_code': forms.NumberInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
        
        }



class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
        widgets = {
        'first_name':forms.TextInput(attrs={
            'class':'form-control rounded-3',
            'id':'floatingInput',
            'required': 'required',
        }),
        'last_name':forms.TextInput(attrs={
            'class':'form-control rounded-3',
            'id':'floatingInput',
            'required': 'required',
        }),
        'email':forms.TextInput(attrs={
            'class':'form-control rounded-3',
            'id':'floatingInput',
            'required': 'required',
        })}


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('address','address2','state','city','zip_code','set_primary')
        widgets = {
            'address': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'address2': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'state': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'city': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'zip_code': forms.NumberInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'set_primart': forms.CheckboxInput(attrs={
                'class':'form-check-input',
                'id':'flexCheckDefault',
                'required':'required',
            }),
        }

class AddressUpdateForm(ModelForm):
    class Meta:
        model = Address
        fields = ('address','address2','state','city','zip_code','set_primary')
        widgets = {
            'address': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'address2': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'state': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'city': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'zip_code': forms.NumberInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'required':'required',
            }),
            'set_primart': forms.CheckboxInput(attrs={
                'class':'form-check-input',
                'id':'flexCheckDefault',
                'required':'required',
            }),
        }

