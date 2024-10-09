from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from AccountApp.forms import LoginForm
from AdminApp.models import LoginTable

# Create your views here.


class HomePage(View):
    def get(self,request):
        return render(request, "home.html")
    

class LoginPage(View):
    def get(self,request):
        return render(request, "login.html")
    def post(self, request):
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        form = LoginForm(request.POST)
        username = request.POST["Username"]
        password = request.POST["Password"]
        if form.is_valid:
            login_obj = LoginTable.objects.get(Username=username, Password=password)
            if login_obj.Type == "admin":
                return HttpResponse('''<script>alert("Welcome to admin home");window.location="/admin_app"</script>''')
            elif login_obj.Type == "staff":
                request.session["login_id"] = login_obj.id
                return HttpResponse('''<script>alert("Welcome to Shop home");window.location="/staff_app"</script>''')

            else:
                return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')
        return HttpResponse('''<script>alert("invalid user");window.location="/"</script>''')



    

    