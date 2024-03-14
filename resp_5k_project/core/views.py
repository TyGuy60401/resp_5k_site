from django.contrib.admin.options import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import U_UserCreationForm, U_AuthenticationForm
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate

# Create your views here.
class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)


class Login(View):
    template = 'login.html'

    def get(self, request):
        form = U_AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = U_AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})

class Register(View):
    template = 'register.html'

    def get(self, request):
        form = U_UserCreationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = U_UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid")
            return HttpResponseRedirect('/login')
        print(form.errors)
        print("I guess it wasn't successfully created")
        return render(request, self.template, {'form': form})
