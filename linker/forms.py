from django import forms

class ProjectForm (forms.Form):
    username = forms.CharField(label="Username")
    repository = forms.CharField(label="Repository")
