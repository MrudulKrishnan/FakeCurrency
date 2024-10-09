from django.contrib import admin
from django.urls import path

from StaffApp.views import *

urlpatterns = [
    path('', StaffHome.as_view(), name="staff_home"),
    path('view_feedback', ViewFeedback.as_view(), name="view_feedback"),
    path('view_notification', ViewNotification.as_view(), name="view_notification"),
    path('view_works', ViewWorks.as_view(), name="view_works"),
    path('update_works/<int:work_id>', ViewWorks.as_view(), name="update_works"),

]
