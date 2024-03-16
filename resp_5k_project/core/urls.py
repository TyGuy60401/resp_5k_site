from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('check_username/', views.check_username),
    path('logout/', views.logout_view),
    path('profile/', views.profile),
    path('hx-profile/', views.hx_profile),
    path('hx-main/', views.main),
]
