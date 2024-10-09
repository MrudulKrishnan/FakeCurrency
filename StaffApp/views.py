from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


from AdminApp.models import *
from StaffApp.form import UpdateStatus

# Create your views here.

class StaffHome(View):
    def get(self, request):
        return render(request, "staff/staff_home.html")
    
class ViewNotification(View):
    def get(self, request):
        obj = NotificationTable.objects.filter(is_active=True)
        return render(request, "staff/view_notification.html", {"noti_obj": obj})
    
    
class ViewFeedback(View):
    def get(self, request):
        obj = FeedbackTable.objects.filter(is_active=True)
        return render(request, "staff/view_feedback.html", {'f_obj': obj})
    
class ViewWorks(View):
    def get(self, request):
        obj = WorkTable.objects.filter(STAFF__LOGIN_id=request.session["login_id"])
        return render(request, "staff/view_assigned_work.html", {"work_obj": obj})
    def post(self, request, work_id):
        obj = WorkTable.objects.get(id=work_id)
        form = UpdateStatus(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Status updated successfully!");window.location="/staff_app/view_works"</script>''')

