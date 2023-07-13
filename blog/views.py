from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, 'blog/about.html', context={"title": "About django"})

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post 
    template_name = "blog/home.html" #we specify this because class based views look under <appname>/<model>_<viewtype.html here that is blog/post_list.html
    context_object_name = "posts"
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    #here we leave template file which will be accessed by this class based view to be default that is blog/post_detail.html

class PostCreateView(LoginRequiredMixin, CreateView): #the LoginRequiredMixin is what @login_required decorator is for a function this is for a class
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #the UserPassesTestMixin helps us validate whether the author of the post is the one trying to update it
    #the LoginRequiredMixin is what @login_required decorator is for a function this is for a class
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):    #this function helps with validating the UserPassesTestMixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #the UserPassesTestMixin helps us validate whether the author of the post is the one trying to delete it
    #the LoginRequiredMixin is what @login_required decorator is for a function this is for a class
    model = Post
    success_url = '/'

    def test_func(self):    #this function helps with validating the UserPassesTestMixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


    

    
    



