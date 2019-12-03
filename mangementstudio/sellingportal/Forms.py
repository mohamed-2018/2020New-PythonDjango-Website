from django import forms
class UserRegister(forms.Form):
    First_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':"form-control"} ))
    Last_name = forms.CharField(required=True,widget=forms.TextInput( attrs={'class':"form-control"} ))
    age = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':"form-control"}  ))
    Data_birth = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':"form-control"}  ))
class DegreeRegister(forms.Form):
    student_Degree =forms.CharField(required=True ,widget=forms.TextInput( attrs={'class':"form-control"} ))

