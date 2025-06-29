from django import forms
from .models import PollingUnit, AnnouncedPuResults

class PollingUnitForm(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields = ['polling_unit_id', 'ward_id', 'lga_id', 'state_id']