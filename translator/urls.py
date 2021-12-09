from . import views
from django.urls import path #function from django to creat url patterns list

urlpatterns = [
    #django will search in the db for slug, amd when found it will execute blogview as view
    #BlogView is taken from the views file, the created class to connect django to the
    #database and connects django to both the html template and the post class create in blog
    #name is needed to point at the url when creating link 
    path('', views.translator_view ,name = 'translator_view')
]

