from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
#this is the second componant, it can be python function or class
# middle man that talks between model and html template  
#views gets the data from model and collects then passes it to the third componant which html template

class BlogView(generic.DetailView): #adding a as view method inside
    model = Post #inherits post from models file
    template_name = 'blog.html' #points to the html template made inside templates 

class AboutView(generic.TemplateView):
    template_name = 'about.html'
    #TemplateView is used when you only need to render a template without getting data from model

class Post_List(generic.ListView): #listview is built to render multiple data rows / post
    queryset = Post.objects.filter(status = 1).order_by('date_created') 
    #get the objects from the post model and get only published and ordered by date created
    template_name = 'index.html'


