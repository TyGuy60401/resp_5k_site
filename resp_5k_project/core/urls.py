from django.urls import path
from . import views


PAGE_TITLES = {
    'profile': f"Profile",
    'main': f"Home",
    'event-info': f"Event Info",
    'live-timing': f"Live Timing",
    'race-route': f"Race Route",
    'contact-us': f"Contact Us",
}

PAGES = [
    'race-route',
    # 'contact-us',
    'event-info',
    'live-timing',
]

urlpatterns = [
    # Login and user auth views
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('logout/', views.logout_view),
    path('check_username/', views.check_username),

    # main page views
    path('', views.Index.as_view()),
    path('profile/', lambda request: views.fill_index_page(request, "/hx-profile/")),

    # hx views
    path('hx-profile/', lambda request: views.hx_profile(request, PAGE_TITLES['profile'])),
    path('hx-main/', lambda request: views.hx_fill_index_page(request, "main.html", PAGE_TITLES['main'])),

    # contact us view
    path('contact-us/', views.ContactUs.as_view()),
    path('hx-contact-us/', views.hx_contact_us),

]

generated_patterns = []

for page in PAGES:
    generated_patterns.append(path(f"{page}/", lambda request, page=page: views.fill_index_page(request, f"/hx-{page}/")))
    generated_patterns.append(path(f"hx-{page}/", lambda request, page=page: views.hx_fill_index_page(request, f"{page}.html", PAGE_TITLES[page])))


urlpatterns += generated_patterns

