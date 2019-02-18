from django import forms

from interests.models import Category

class InterestsForm(forms.Form):
    personal_interests = forms.ModelMultipleChoiceField(
     widget=forms.CheckboxSelectMultiple,
     queryset=Category.objects.all().order_by('name'),
     required=False,
     label='Interests')

    class Meta:
        model = Category
        # fields = ('object_class', 'objeto', 'severity', 'message', 'email_template', 'internal_notification', 'client_notification',
        # 'notification_timetable', 'internal_escalation', 'client_escalation', 'escalation_timetable', 'localization',
        # 'assignment', 'procedure', 'snmp', 'ci_group')
