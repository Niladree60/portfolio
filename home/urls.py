from django.contrib import admin
from django.urls import path,include
from home import views

#django admin header customization 
admin.site.site_header = "Login to Developer Niladree"
admin.site.site_title = "Welcome to Niladree's Dashboard "
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('projects', views.projects, name = 'projects'),
    path('contact', views.contact, name = 'contact'),
]
