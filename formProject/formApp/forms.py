from django import forms


#Create class

class empInfoForm (forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField() 
