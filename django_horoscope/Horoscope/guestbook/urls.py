from django.urls import path
from .views import (PostentryListView)

app_name = 'guestbook'

urlpatterns = [
path('', PostentryListView.as_view(), name='guestbook')
]
