from django.contrib.admin.options import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.utils.text import wrap
from django.views import View
from django.contrib.auth.views import FormView, LoginView
from django.contrib.auth import get_user_model, logout
from django.http.response import HttpResponse
from django.urls import reverse_lazy


from .mixins import U_LoginRequiredMixin
from .forms import U_SendUsMessage, U_UserCreationForm, U_AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

SITE_TITLE = "WSU Respiratory 5K"

def get_context(added_context=None) -> dict:
    context = {
        "site_title": SITE_TITLE,
    }
    if added_context:
        context.update(added_context)
    return context

# Create your views here.
class Index(View):
    template = 'index.html'
    # login_url = '/login/'

    def get(self, request):
        return render(request, self.template, get_context())

def fill_index_page(request, hx_path_name):
    context = get_context({
        "main_content_path": hx_path_name
    })
    return render(request, 'index.html', context)

def hx_fill_index_page(request, page_name, title):
    print(page_name, title)
    return render(request, page_name, context=get_context({"title": f"{title} - {SITE_TITLE}"}))

def hx_profile(request, title):
    if request.user.id == None:
        # return HttpResponse('<p>You must be logged in to view this page</p><br><a href="/login/">Log in</a>')
        return render(request, 'not-logged-in.html', context=get_context({"not_logged_in_title": "Profile"}))
    else:
        return render(request, 'profile.html', context=get_context({"title": f"{title} - {SITE_TITLE}"}))

def hx_contact_us(request):
    form = U_SendUsMessage()
    return render(request, 'contact-us.html', get_context({'form': form}))


class ContactUs(View):
    template = 'index.html'
    form_class = U_SendUsMessage


    def get(self, request):
        form = U_SendUsMessage()
        return render(request, self.template, get_context({'form': form, 'main_content_path': '/hx-contact-us/'}))

    def post(self, request):
        form = U_SendUsMessage(request.POST)
        if form.is_valid():
            # form.save()
            print("Form is valid")
            return HttpResponseRedirect('/message-sent/')
        print(form.errors)
        return render(request, self.template, get_context({'form': form, 'main_content_path': '/hx-contact-us/'}))



class Login(LoginView):
    template_name = 'login.html'
    form_class = U_AuthenticationForm

class Register(View):
    template = 'register.html'

    def get(self, request):
        form = U_UserCreationForm()
        return render(request, self.template, get_context({'form': form}))

    def post(self, request):
        form = U_UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid")
            return HttpResponseRedirect('/login')
        print(form.errors)
        print("I guess it wasn't successfully created")
        return render(request, self.template, get_context({'form': form}))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div class="alert alert-warning" role="alert" id="username-error">This username already exists</div>')
    else:
        return HttpResponse('')
