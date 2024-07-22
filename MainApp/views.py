from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect

from .forms import UserRegistrationForm
from django.views.generic import View


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username =", username)
        print("password =", password)
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
        else:
            return redirect('/login')

    return redirect('/')


def login_form(request):
    return render(request, 'login_form.html', {})


def home_form(request):
    return render(request, 'home_form.html', {})


def logout(request):
    auth.logout(request)

    return redirect('/')


def UserRegistrationView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()


# class UserRegistrationView(View):
#     def post(self, request):
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/")
# Create your views here.
