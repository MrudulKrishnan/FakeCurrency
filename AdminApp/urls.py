from django.contrib import admin
from django.urls import path

from AdminApp.views import *

urlpatterns = [
    path('', AdminHome.as_view(), name="admin_home"),
    path('view_users/', ViewUser.as_view(), name="view_user"),
    path('manage_staff/', ManageStaff.as_view(), name="manage_staff"),
    path('add_staff/', AddStaff.as_view(), name="add_staff"),
    path('edit_staff/<int:staff_id>', EditStaff.as_view(), name="edit_staff"),
    path('delete_staff/<int:staff_id>', DeleteStaff.as_view(), name="delete_staff"),
    path('view_feedback', ViewFeedback.as_view(), name="view_feedback"),
    path('send_notification', SendNotification.as_view(), name="send_notification"),
    path('delete_notification/<int:noti_id>', DeleteNotification.as_view(), name="delete_notification"),
    path('assign_work', AssignWorkStaff.as_view(), name="assign_work"),
    path('view_complaints', ViewComplaints.as_view(), name="view_complaints"),
    path('send_reply/<int:comp_id>', ViewComplaints.as_view(), name="send_reply"),
]
