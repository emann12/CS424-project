from django import forms

from members.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        #exclude=['date_of_birth']
        fields = ['first_name','last_name']