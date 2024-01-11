from django.urls import path
from . import views as v

app_name = 'feature'
urlpatterns = [
    path('customize/',v.Customisation,name="customization"),
    path('about/',v.About,name="about"),
    path('contact/',v.Contact,name="contact"),
    path('project/',v.Project,name="project"),    
]