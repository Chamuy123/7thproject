from rcb.views import *

from django.urls import path

app_name='anythong'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('siraj/',siraj,name='siiraj'),
]