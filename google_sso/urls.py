from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    # path('logout/', logout_view, name='logout'),
    path('test/', test, name="test"),
    path('testList/', testList, name="testList"),
]