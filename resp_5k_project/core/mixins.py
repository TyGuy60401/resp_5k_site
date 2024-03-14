from django.contrib.admin.options import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class U_LoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login/')
        return super().dispatch(request, *args, **kwargs)
