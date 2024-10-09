from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from AdminApp.forms import *
from AdminApp.models import *

# Create your views here.

class AdminHome(View):
    def get(self, request):
        return render(request, "admin/admin_home.html")
    
class ViewUser(View):
    def get(self, request):
        val = UserTable.objects.filter(is_active=True)
        return render(request, "admin/view_users.html", {"key": val})
    
class ManageStaff(View):
    def get(self, request):
        value = StaffTable.objects.filter(is_active=True)
        return render(request, "admin/manage_staff.html", {"key": value}) 
    
class AddStaff(View):
    def get(self, request):
        return render(request, "admin/add_new_staff.html")  
    def post(self, request):
        form = AddStaffForm(request.POST)
        if form.is_valid:

            staff = form.save(commit=False)

            login_obj = LoginTable()
            login_obj.Username = request.POST["Username"]
            login_obj.Password = request.POST["Password"]
            login_obj.Type = "staff"
            login_obj.save()
            staff.LOGIN = login_obj
            staff.save()
            return HttpResponse('''<script>alert("Staff added successfully!");window.location="/admin_app/manage_staff"</script>''')
        else:
            # Print form errors to help debug
            print("Form errors:", form.errors)
            return render(request, "admin/add_new_staff.html", {'form': form})
 


class EditStaff(View):
    def get(self, request, staff_id):
        staff_obj = StaffTable.objects.get(id=staff_id)
        return render(request, "admin/edit_staff.html", {'key': staff_obj})
    def post(self, request, staff_id):
        staff_obj = StaffTable.objects.get(id=staff_id)
        form = AddStaffForm(request.POST, instance=staff_obj)
        if form.is_valid:
            
            staff = form.save(commit=False)
            staff.save()
            return HttpResponse('''<script>alert("Staff Edited successfully!");window.location="/admin_app/manage_staff"</script>''')
        else:
            # Print form errors to help debug
            print("Form errors:", form.errors)
            return render(request, "admin/add_new_staff.html", {'form': form})


class DeleteStaff(View):
    def get(self, request, staff_id):
        staff_obj = StaffTable.objects.get(id=staff_id)
        staff_obj.is_active = False
        staff_obj.save()
        return HttpResponse('''<script>alert("Staff deleted successfully!");window.location="/admin_app/manage_staff"</script>''')

    

class ViewFeedback(View):
    def get(self, request):
        obj = FeedbackTable.objects.filter(is_active=True)
        return render(request, "admin/view_feedback.html", {"key": obj})    
        
class SendNotification(View):
    def get(self, request):
        notifications_obj = NotificationTable.objects.filter(is_active=True)
        return render(request, "admin/send_notification.html", {"notifications":notifications_obj})
    def post(self, request):
        form = NotificationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse('''<script>alert("Notification sent successfully!");window.location="/admin_app/manage_staff"</script>''')


class DeleteNotification(View):
    def get(self, request, noti_id):
        notifications_obj = NotificationTable.objects.get(id=noti_id)
        notifications_obj.is_active = False
        notifications_obj.save()
        return HttpResponse('''<script>alert("Notification Deleted successfully!");window.location="/admin_app/send_notification"</script>''')

            
class AssignWorkStaff(View):
    def get(self, request):
        staff_obj = StaffTable.objects.filter(is_active=True)
        work_obj = WorkTable.objects.filter(is_active=True)
        return render(request, "admin/assign_work_to_staff.html", {"key": staff_obj, "work": work_obj})
    def post(self, request):
        form = WorkAssignForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            staff_id = request.POST["Staff"]
            form_obj.STAFF=StaffTable.objects.get(id=staff_id)
            form_obj.Status = "pending"
            form_obj.save()
            return HttpResponse('''<script>alert("Work assigned successfully!");window.location="/admin_app/assign_work"</script>''')
        return HttpResponse('''<script>alert("Form not valid!");window.location="/admin_app/assign_work"</script>''')

    
class ViewComplaints(View):
    def get(self, request):
        comp_obj = ComplaintTable.objects.filter(is_active=True)
        return render(request, "admin/view_complaints_reply.html", {"comp": comp_obj})
    def post(self, request, comp_id):
        comp_obj = ComplaintTable.objects.get(id=comp_id)
        form = ComplaintForm(request.POST, instance=comp_obj)
        if form.is_valid():
            reply = request.POST["Reply"]
            form.Reply = reply
            form.save()
            return HttpResponse('''<script>alert("Reply sent successfully");window.location="/admin_app/view_complaints"</script>''')



        