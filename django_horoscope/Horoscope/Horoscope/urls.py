"""Horoscope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pages.views import home_view, zodiac_page_view, contact_page_view, game_page_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home_view, name ='home'),
    path('home/', home_view, name ='home'),
    path('zodiac/', zodiac_page_view, name ='zodiac'),
    path('contact/', contact_page_view, name ='contact'),
    path("<int:id_>", zodiac_page_view, name ='zodiac2'), 
    path("guestbook/", include("guestbook.urls")),
    path('admin/', admin.site.urls),
    path('guestbook/game/', game_page_view),
 
]

urlpatterns += staticfiles_urlpatterns()

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)