from django import forms
from datetime import date
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < date.today():
            self.instance.status = 'Overdue'
        elif due_date and due_date == date.today():
            self.instance.status = 'Due Today'
        else:
            self.instance.status = 'Upcoming'
        return due_date


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search by title...'})
    )