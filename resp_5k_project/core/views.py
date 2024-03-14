from django.contrib.admin.options import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model, logout
from django.http.response import HttpResponse
from django.urls import reverse_lazy


from .mixins import U_LoginRequiredMixin
from .forms import U_UserCreationForm, U_AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Index(View):
    template = 'index.html'
    # login_url = '/login/'

    def get(self, request):
        return render(request, self.template)

def main(request):
    return render(request, 'main.html')

def profile(request):
    if request.user.id == None:
        return HttpResponse('<p>You must be logged in to view this page</p><br><a href="/login/">Log in</a>')
    else:
        return render(request, 'profile.html')

class Login(LoginView):
    template_name = 'login.html'
    form_class = U_AuthenticationForm
    

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div class="alert alert-warning" role="alert" id="username-error">This username already exists</div>')
    else:
        return HttpResponse('')

