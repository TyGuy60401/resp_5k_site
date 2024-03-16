from django.urls import path
from . import views

urlpatterns = [
    # Login and user auth views
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('logout/', views.logout_view),
    path('check_username/', views.check_username),

    # main page views
    path('', views.Index.as_view()),
    path('profile/', lambda request: views.fill_index_page(request, "/hx-profile/")),
    path('general-info/', lambda request: views.fill_index_page(request, "/hx-general-info/")),
    path('live-timing/', lambda request: views.fill_index_page(request, "/hx-live-timing/")),
    path('race-route/', lambda request: views.fill_index_page(request, "/hx-race-route/")),

    # hx views
    path('hx-profile/', views.hx_profile),
    path('hx-main/', lambda request: views.hx_fill_index_page(request, "main.html")),
    path('hx-general-info/', lambda request: views.hx_fill_index_page(request, "general-info.html")),
    path('hx-live-timing/', lambda request: views.hx_fill_index_page(request, "live-timing.html")),
    path('hx-race-route/', lambda request: views.hx_fill_index_page(request, "race-route.html")),
]
