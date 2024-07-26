from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createProduct, name='createProduct'),
    path('list', views.listProduct, name='listProduct'),
    path('detail/<int:id>/', views.detailProduct, name='detailProduct'),
    path('delete/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('enter', views.storyEnter, name='storyEnter'),
    path('createenter', views.createEnter, name = 'createEnter'),
    path('delete/<int:id>/', views.enterDelete, name = 'enterDelete'),
    path('updateenter', views.updateEnter, name = 'updateEnter'),    
]