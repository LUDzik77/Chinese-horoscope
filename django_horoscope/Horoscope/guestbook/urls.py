from django.urls import path
from pages.views import game_page_view
from .views import (
    PostentryListView,
    PostentryCreateView)


app_name = 'guestbook'
urlpatterns = [
    path('', PostentryListView.as_view(), name='Postentry-list'),
    path('create/', PostentryCreateView.as_view(), name='Postentry-create'),
    path('game/', game_page_view),
    path('create/game/', game_page_view)
]