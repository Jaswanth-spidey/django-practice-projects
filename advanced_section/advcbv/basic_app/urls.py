from django.urls import re_path
from . import views


urlpatterns =[
    re_path(r'^$',views.Schoollist.as_view(), name='list'),
    re_path(r'^update/(?P<pk>[\d]+)/$',views.SchoolUpdateView.as_view(), name='update'),
    re_path(r'^create/$',views.SchoolCreateView.as_view(), name='create'),
    re_path(r'^detial_view/(?P<pk>[-\w]+)/$', views.Schooldetailview.as_view(), name='detail_view'),
    
    
]