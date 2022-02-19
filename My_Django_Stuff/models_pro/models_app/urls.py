from django.conf.urls import include
from models_app import views

urlpatterns = [
    path('',views.index,name='index'),
]