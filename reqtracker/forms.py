#from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#Form for user's 
class MainRequestForm(forms.ModelForm):
    class Meta:
        model = MainRequest
        fields = ['Request_Number','Maintenance','Maintenance_Type','Nature_Civil','Nature_MEP','Type_Nature','Zone','Flat','Building','Floor','Complaint_Details']

#Form for clients	
class MainRequestFormAdmin(forms.ModelForm):
    class Meta:
        model = MainRequest
        fields = ['Request_Number','Maintenance','Maintenance_Type','Nature_Civil','Nature_MEP','Type_Nature','Zone','Flat','Building','Floor','Complaint_Details','status']

#Form for registration
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("first_name","last_name","username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
        
class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = MainRequest
        fields = ('Request_Number','status')
        
class CompletionForm(forms.ModelForm):
    class Meta:
        model = Completion
        fields = ('mr','tech_name','item','quantity','unit','work_details')