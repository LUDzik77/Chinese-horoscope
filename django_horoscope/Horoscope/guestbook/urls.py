from django.urls import path
from .views import (
    PostentryListView,
    PostentryCreateView
)

app_name = 'guestbook'
urlpatterns = [
    path('', PostentryListView.as_view(), name='Postentry-list'),
    path('create/', PostentryCreateView.as_view(), name='Postentry-create')
]