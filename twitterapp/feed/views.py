
from dataclasses import field, fields
from datetime import datetime
from msilib.schema import ListView
from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView,CreateView,UpdateView
from django .contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class TweetListView(LoginRequiredMixin,ListView):
    model = tweet 
    template_name= 'feed/home.html'
    ordering = ['-datetime']

class TweetCreateView(LoginRequiredMixin,CreateView):
    model = tweet
    fields = ['text']
    success_url = '/'
    def form_valid(self,form):
        form.instance.uname = self.request.user
        return super().form_valid(form)
class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = tweet
    fields = ['text']
    success_url = '/'
    def form_valid(self,form):
            
        form.instance.uname = self.request.user
        return super().form_valid(form)
           
    def test_func(self):
        tweet= self.get_object()
        if (self.request.user ==tweet.uname):

            return True
        return False
    
   