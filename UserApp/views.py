import json
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from AdminApp.models import Token
from UserApp.serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from django.contrib.auth import authenticate, login

from UserApp.serializers import UserSerializer



# Create your views here.



# ///////////////////////////// API ///////////////////////////////////////////////////////


class UserReg(APIView):
    def post(self, request):
        print("###############",request.data)
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            hashed_password = make_password(request.data['Password'])
            login_profile = login_serial.save(Type='USER', Password=hashed_password, status='Approve')
            user_serial.save(LOGIN=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)



class LoginPage(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = tuple()

    def get(self, request):
        response_dict = {"status": "REJECT"}
        response_dict["logged_in"] = bool(request.user.is_authenticated)

        response_dict["status"] = "APPROVE"
        return Response(response_dict, HTTP_200_OK)

    def post(self, request):
        response_dict = {"status": "REJECT", "token": None, "redirect": False}
        password = request.data.get("Password")
        print("*****************",password)
        username = request.data.get("Username")
        print("$$$$$$$$$$$$$",username)
        try:
            t_user = LoginTable.objects.filter(Username=username).first()
            print("user_obj :-----------", t_user)
            response_dict["session_data"] = {
                "user_id": t_user.id,
                "user_type": t_user.Type,
            }
            print("dict:-----------", response_dict)
            return Response(response_dict, HTTP_200_OK)

        except LoginTable.DoesNotExist:
            response_dict[
                "reason"
            ] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
        # blocked_msg = "This account has been blocked. Please contact admin."
        # today = utc_today()
        # authenticated = authenticate(username=t_user.Username, password=password)

        # if not authenticated:
        #     print("notttttttttttttt")
        #     response_dict["reason"] = "Invalid credentials."
        #     # return Response(response_dict, HTTP_200_OK)

        # user = t_user
        # print("%%%%%%%%%%%%",t_user.status)
        # if user.status == "Approve":
        #     # session_dict = {"real_user": authenticated.id}
        #     token, _ = Token.objects.get_or_create(user=user, defaults={"session_dict": json.dumps(session_dict)})
        #     login(request, user, "django.contrib.auth.backends.ModelBackend")
        #     response_dict["session_data"] = {
        #         "user_id": user.id,
        #         "user_type": user.user_type,
        #         "token": token.key,
        #         "username": user.username,
        #         "name": user.first_name,
        #         "status": user.status,
        #     }

        #     response_dict["token"] = token.key
        #     response_dict["status"] = True

        #     return Response(response_dict, HTTP_200_OK)
        # else:
        #     response_dict["reason"] = "Your account has not been approved yet or you are a CLIENT user."
        #     return Response(response_dict, HTTP_200_OK)
            # # if user.status != "APPROVE":
            # #     print("apppppppp")
            # #     response_dict["reason"] = "Your account has not been approved yet. Please contact admin."
            # #     return Response(response_dict, HTTP_200_OK)
            #
            # session_dict = {"real_user": authenticated.id}
            # token, _ = Token.objects.get_or_create(
            #     user=user, defaults={"session_dict": json.dumps(session_dict)}
            # )
            # login(request, user, "django.contrib.auth.backends.ModelBackend")
            # response_dict["session_data"] = {
            #     "user_id": user.id,
            #     "user_type": user.user_type,
            #     "token": token.key,
            #     "username": user.username,
            #     "name": user.first_name,
            #     "status": user.status,
            # }
            #
            # response_dict["token"] = token.key
            # response_dict["status"] = "APPROVE"
            # print(response_dict)
            #
            # return Response(response_dict, HTTP_200_OK)

class SendComplaint(APIView):
    def get(self, request):
        obj = ComplaintTable.objects.all()
        print("%%%%%%%%%%%%%%",obj)
        complaint_serializer = ComplaintSerializer(obj, many=True)
        return Response(complaint_serializer.data)
    def post(self, request):
        comp_serializer = ComplaintSerializer(data=request.data)
        user = request.data['USER']
        user_obj = UserTable.objects.get(LOGIN_id=user)
        if comp_serializer.is_valid():
            comp_serializer.save(USER=user_obj)
            return Response(comp_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comp_serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        
class SendFeedback(APIView):
    def get(self, request):
        obj = FeedbackTable.objects.all()
        feedback_serializer = FeedbackSerializer(obj, many=True)
        print("&&&&&&&&&&", feedback_serializer)
        return Response(feedback_serializer.data)
    def post(self, request):
        feedback_obj = FeedbackPostSerializer(data=request.data)
        user_id = request.data['USER']
        print('#########', user_id)
        print('$$$$$$$$$$', feedback_obj)
        user_obj = UserTable.objects.get(LOGIN_id=request.data['USER'])
        if feedback_obj.is_valid():
            feedback_obj.save(USER=user_obj)
            return Response(feedback_obj.data, status=status.HTTP_201_CREATED)
        else:
            return Response(feedback_obj.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        




