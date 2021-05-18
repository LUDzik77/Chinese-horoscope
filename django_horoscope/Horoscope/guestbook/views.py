from django.shortcuts import render

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Postentry

class PostentryListView(ListView):
    template_name = 'guestbook/Postentry_list.html'
    queryset = Postentry.objects.all()  #guestbook/Postentry_list.html