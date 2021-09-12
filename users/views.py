from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationsForm, LoginForm
from django.contrib import messages


class UserRegistrationView(View):
    """ User Registration View """
    template_name = 'register.html'
    form_class = UserRegistrationsForm()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        parameter: username, password
        """

        form = UserRegistrationsForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=user.password)
            login(request, user)
            messages.info(request, f"You are now logged in as {user.username}.")
            return redirect('/')
        return render(request, self.template_name, {'form': form})


def login_view(request):
    """ view for user login """
    form = LoginForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # authenticate using custom authentication backend
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, f"You are now logged in as {user.username}.")
            return redirect('/')
        else:
            return redirect('login')
    return render(request, 'login.html', {'form': form})



# def logout_view(request):
#     """
#     user logout view
#     """
#     logout(request)
#     return redirect('login')
