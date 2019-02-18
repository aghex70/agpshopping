from django import forms

from interests.models import Category

class InterestsForm(forms.Form):
    personal_interests = forms.ModelMultipleChoiceField(
     widget=forms.CheckboxSelectMultiple,
     queryset=Category.objects.all().order_by('name'),
     required=False,
     label='Interests')
