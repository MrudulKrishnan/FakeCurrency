
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from AdminApp.models import *
class UserSerializer(ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['Firstname', 'Lastname', 'Gender', 'Age', 'Place', 'Post', 'Pin', 'Phone', 'Email']


class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['Username', 'Password']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['Complaint', 'Reply']

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedbackTable
        fields = ['Feedback', 'Rating', 'created_at']

class FeedbackPostSerializer(ModelSerializer):
    class Meta:
        model = FeedbackTable
        fields = ['Feedback', 'Rating']


