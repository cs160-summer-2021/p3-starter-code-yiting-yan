from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('palette', views.palette, name='palette'),
    path('new_interaction', views.new_interaction, name='new_interaction')
]
