from django.urls import path
from . import views

TITLE_SUFFIX = " - WSU Respiratory 5k"

PAGE_TITLES = {
    'profile': f"Profile{TITLE_SUFFIX}",
    'main': f"Home{TITLE_SUFFIX}",
    'general-info': f"General Info{TITLE_SUFFIX}",
    'live-timing': f"Live Timing{TITLE_SUFFIX}",
    'race-route': f"Race Route{TITLE_SUFFIX}",
    'contact-us': f"Contact Us{TITLE_SUFFIX}",
}

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
    path('contact-us/', lambda request: views.fill_index_page(request, "/hx-contact-us/")),

    # hx views
    path('hx-profile/', lambda request: views.hx_profile(request, PAGE_TITLES['profile'])),
    path('hx-main/', lambda request: views.hx_fill_index_page(request, "main.html", PAGE_TITLES['main'])),
    path('hx-general-info/', lambda request: views.hx_fill_index_page(request, "general-info.html", PAGE_TITLES['general-info'])),
    path('hx-live-timing/', lambda request: views.hx_fill_index_page(request, "live-timing.html", PAGE_TITLES['live-timing'])),
    path('hx-race-route/', lambda request: views.hx_fill_index_page(request, "race-route.html", PAGE_TITLES['race-route'])),
    path('hx-contact-us/', lambda request: views.hx_fill_index_page(request, "contact-us.html", PAGE_TITLES['contact-us'])),
]
