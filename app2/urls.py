app_name='app2'
from django.urls import path
from app2.views import *

urlpatterns=[
    path('details/',details,name='details'),
]