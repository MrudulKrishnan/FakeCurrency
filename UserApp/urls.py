from django.urls import path

from UserApp.views import LoginPage, SendComplaint, SendFeedback, UserReg


urlpatterns = [
    path("user_register", UserReg.as_view(), name="user_register"),
    path("login_page", LoginPage.as_view(), name="login_page"), 
    path("send_complaint", SendComplaint.as_view(), name="send_complaint"), 
    path("send_feedback", SendFeedback.as_view(), name="send_feedback"), 
]
