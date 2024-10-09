import json
import random
import string
from django.db import models

# Create your models here.

USER_TYPE_CHOICES = {

    ("ADMIN", "admin"),
    ("USER", "user"),
    ("FARMER", "farmer")

}

STATUS_CHOICES = {

    ("ACTIVE", "Active"),
    ("DEACTIVE", "Deactive"),
}

class LoginTable(models.Model):
    Username = models.CharField(max_length=30, blank=True, null=True)
    Password = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES)

    Type = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, models.CASCADE)
    Firstname = models.CharField(max_length=30, blank=True, null=True)
    Lastname = models.CharField(max_length=30, blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=30, blank=True, null=True)
    Place = models.CharField(max_length=50, blank=True, null=True)
    Post = models.CharField(max_length=50, blank=True, null=True)
    Pin = models.IntegerField(blank=True, null=True)
    Phone = models.BigIntegerField(blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Token(models.Model):
    key = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(
        UserTable,
        related_name="auth_tokens",
        on_delete=models.CASCADE,
        verbose_name="user",
        unique=True,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(null=False, default="{}")

    def generate_key(self):
        """Generate a random key for the token."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    def read_session(self):
        """Read session data from the session_dict attribute."""
        try:
            self.data_dict = json.loads(self.session_dict)
        except json.JSONDecodeError:
            self.data_dict = {}

    def write_back(self):
        """Write session data back to the session_dict attribute."""
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        """Get a value from the session data."""
        self.read_session()
        return self.data_dict.get(key, default)

    def set(self, key, value, save=True):
        """Set a value in the session data."""
        self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def update_session(self, tdict, save=True, clear=False):
        """Update session data with the provided dictionary."""
        self.read_session()
        if clear:
            self.data_dict = tdict
        else:
            self.data_dict.update(tdict)
        if save:
            self.write_back()

    def save(self, *args, **kwargs):
        """Override the save method to generate a key if not provided."""
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def str(self):
        """Return a string representation of the token."""
        return str(self.user) if self.user else str(self.id)


class StaffTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, models.CASCADE)
    Firstname = models.CharField(max_length=30, blank=True, null=True)
    Lastname = models.CharField(max_length=30, blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=30, blank=True, null=True)
    Place = models.CharField(max_length=50, blank=True, null=True)
    Post = models.CharField(max_length=50, blank=True, null=True)
    Pin = models.IntegerField(blank=True, null=True)
    Phone = models.BigIntegerField(blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class FeedbackTable(models.Model):
    USER = models.ForeignKey(UserTable, models.CASCADE)
    Feedback = models.CharField(max_length=300, blank=True, null=True)
    Rating = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class NotificationTable(models.Model):
    Subject = models.CharField(max_length=300, blank=True, null=True)
    Notification = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class WorkTable(models.Model):
    STAFF = models.ForeignKey(StaffTable, models.CASCADE)
    Work = models.CharField(max_length=100, blank=True, null=True)
    Description = models.CharField(max_length=300, blank=True, null=True)
    Status = models.CharField(max_length=100, blank=True, null=True)
    Deadline = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class ComplaintTable(models.Model):
    USER = models.ForeignKey(UserTable, models.CASCADE)
    Complaint = models.CharField(max_length=200, blank=True, null=True)
    Reply = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)



