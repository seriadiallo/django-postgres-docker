from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect


from .forms import UserForm, UserLoginForm


def create_user(request):
    if request.user.is_authenticated:
        return redirect('list-articles-class')
    if request.method == 'GET':
        form = UserForm()
    elif request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User.objects.create_user(
                username=cleaned_data.get('username'),
                email=cleaned_data.get('email'),
                password=cleaned_data.get('password')
            )
            user.first_name = cleaned_data.get('first_name')
            user.last_name = cleaned_data.get('last_name')
            user.save()
            return redirect('list-articles-class')
    data = {
        'form': form
    }
    return render(
        context=data, request=request, template_name='accounts/creation.html'
        )


def login_user(request):
    if request.user.is_authenticated:
        return redirect('list-articles-class')
    if request.method == "GET":
        form = UserLoginForm()
    elif request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request, username=username, password=password
                )
            if user is not None:
                login(request=request, user=user)
                return redirect('list-articles-class')

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
