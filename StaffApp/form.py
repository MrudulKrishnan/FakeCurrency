from django.forms import ModelForm

from AdminApp.models import WorkTable


class UpdateStatus(ModelForm):
    class Meta:
        model = WorkTable
        fields = ["Status"]
