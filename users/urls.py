# urls
from django.urls import path

# views
from users.views import sing_in, sing_up

app_name = 'users'

urlpatterns = [
    path('sing_in/', sing_in, name='sing_in'),
    path('sing_up/', sing_up, name='sing_up'),
]