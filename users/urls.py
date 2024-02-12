from django.urls import path
from .views import *

app_name = 'users'


urlpatterns = [
    path('', sign_in, name='signin'),
    path('signup/', sign_up, name='sign_up')
]