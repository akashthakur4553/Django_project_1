from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    # print(
    #     "hello i ma registration modeule----------------------------------------------------------------------------------------------------------------------------"
    # )
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["username"]
        user_data_error = False
        if User.objects.filter(username=username).exists():
            messages = "username already exists"
            user_data_error = True
        if User.objects.filter(email=email).exists():
            messages = "Email already exists"
            user_data_error = True
        if user_data_error:
            return render(request, "register.html", {"messages": messages})

        if not user_data_error:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            messages = f"Sucessfully registered {first_name}"
            return redirect("login_view")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("Home")
        else:
            messages = "Invalid Login Credentials"
            return render(request, "login.html", {"messages": messages})

    return render(request, "login.html")


def Home(request):

    return render(request, "Home.html")


def Logout_view(request):
    logout(request)
    return redirect("login_view")
