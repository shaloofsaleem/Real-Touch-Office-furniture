from django.urls import path
from . import views as v

app_name = 'account'
urlpatterns = [
    path('login/',v.LoginPage ,name='login'),
    path('signup/',v.SignupPage, name= 'signup'),
    path('activate/<email_token>/',v.activation_mail, name= 'activate'),


     
]