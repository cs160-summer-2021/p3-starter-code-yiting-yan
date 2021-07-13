from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('palette', views.palette, name='palette'),
    path('new_interaction', views.new_interaction, name='new_interaction')
]
