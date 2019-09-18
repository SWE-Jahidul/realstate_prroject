from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('buy',views.buy,name='buy'),
    path('rent',views.rent,name='rent'),
    path('blog',views.blog,name='blog'),
    path('contract',views.contract,name='contract'),
    path('about',views.about,name='about'),
    path('serch',views.serch,name='serch'),
    
    path('base',views.serch,name='base'),
]