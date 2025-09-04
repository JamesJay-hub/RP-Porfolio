from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter Project Title',
                'style': 'width:300px; padding:4px;'})
            # 'description': forms.TextInput(attrs={
            #     'placeholder': 'Enter project description',
            #     'style': 'width:400px; padding:10px;'
            # })
        }