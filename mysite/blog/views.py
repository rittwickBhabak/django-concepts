from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView 
from .models import Post 

class AllPost(ListView):
    model = Post 

class TaggedPosts(ListView):
    model = Post 
    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs['tag']])
    

class ViewPost(DetailView):
    model = Post 

class UpdatePost(UpdateView):
    model = Post 
    fields = ["title", "content", "tags"]

class CreatePost(CreateView):
    model = Post 
    fields = ["title", "content", "tags"]

class RemovePost(DeleteView):
    model = Post 
    success_url = reverse_lazy("blog:list")