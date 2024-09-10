from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']
        Widgets = {'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),}