from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin): #special class inherited for admin models
    list_display = ('title','date_created','author')


#Register your models here.
#code for admin interface

admin.site.register(Post,PostAdmin) #calling the class created also in the register