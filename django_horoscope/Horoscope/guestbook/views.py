from django.shortcuts import render

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import PostentryModelForm
from .models import Postentry

class PostentryListView(ListView):
    template_name = 'guestbook/Postentry_list.html'
    queryset = Postentry.objects.all()  

class PostentryCreateView(CreateView):
    template_name = 'guestbook/Postentry_create.html'
    form_class = PostentryModelForm
    queryset = Postentry.objects.all()
    success_url = '/guestbook'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return (super().form_valid(form))
    