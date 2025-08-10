from django import forms
from django.core.exceptions import ValidationError

from core.apps.dds.models.dds import DDS


class DDSAdminForm(forms.ModelForm):
    class Meta:
        model = DDS
        fields = '__all__'

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("Сумма должна быть положительной")
        return amount
