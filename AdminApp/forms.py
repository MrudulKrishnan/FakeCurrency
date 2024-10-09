
from django.forms import ModelForm

from AdminApp.models import *


class AddStaffForm(ModelForm):
    class Meta:
        model = StaffTable
        fields = ["Firstname", "Lastname", "Age", "Gender", "Place", "Post", "Pin", "Phone",
                   "Email"]
        
class WorkAssignForm(ModelForm):
    class Meta:
        model = WorkTable
        fields = ["Work", "Description", "Deadline"]        
        
class NotificationForm(ModelForm):
    class Meta:
        model = NotificationTable
        fields = ['Subject','Notification']  

class ComplaintForm(ModelForm):
    class Meta:
        model = ComplaintTable
        fields = ["Reply"]           
