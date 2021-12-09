from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#django sees a website as 3 things, MODEL database field of the webpage

STATUS = ((0,'Draft'),(1,'Publish'))
class Post(models.Model): #models is created by django devs, Model is a method in models
    #designed to contain fields of data
    #Post creates a new table in sqlite
    title = models.CharField(max_length = 200) #text box allows 200 characyers for title of blog
    #charfield is designed for small length of text
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True) #date time field, adding time when content will
    #be created, the class will be instantiated creating the current date time and will be injected into 
    #the field of the sql table
    slug = models.SlugField(max_length=200, unique=True) #this is the url that follows the original for the blog post
    #url after the domain, creator can add whatever to create the slug name
    #unique makes sure pages cannot have the same url 
    author = models.ForeignKey(to=User, on_delete = models.CASCADE) #value of db field will come from a another db table
    #if a user is deleted, the cascade meanss that the users post will also be deleted
    status = models.IntegerField(choices=STATUS,default=0) #status dropdown list will have draft and publish, 
    #created above, STATUS will mean the admin will see either draft or publish 0 or 1
    #default is draft

    def __str__(self):
        return self.title

#using the command python manage.py makemigrations to create the post table and change db struct
#then python manage.py migrate to apply the sql migrations