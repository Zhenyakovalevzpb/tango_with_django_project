from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
]
