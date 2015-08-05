from django import forms
from conjugate.models import Verb

class ChoicesForm(forms.Form):
    briathar = forms.ModelChoiceField(queryset=Verb.objects.all().order_by('verb'))
