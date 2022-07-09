from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView 
from .models import Post 

class AllPost(ListView):
    model = Post 

class ViewPost(DetailView):
    model = Post 

class UpdatePost(UpdateView):
    model = Post 
    fields = ["title", "content"]

class CreatePost(CreateView):
    model = Post 
    fields = ["title", "content"]

class RemovePost(DeleteView):
    model = Post 
    success_url = reverse_lazy("blog:list")