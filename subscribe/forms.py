from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Subscribe


class SubscribeForms(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = "__all__"
        # exclude = ('first_name',)
        labels = {
            'first_name':_('Enter First Name'),
            'last_name':_('Enter Last Name'),
            'email':_('Enter Your Email')
        }
        
        error_messages ={
            'first_name':{
                'requried':_("you can not move forward without first name")
            }
        }

        

# def validate_comma(value):
#    if ',' in value:
#        raise forms.ValidationError('Invalid last name')
#    return value
   

# class SubscribeForms(forms.ModelForm):
#     first_name = forms.CharField(max_length=200, label='Enter First Name: ', help_text='Enter Your First Name!!')
#     last_name = forms.CharField(max_length=200, disabled= False, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)



