from django.urls import path
from . import views

app_name = "restaurants"
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('signup/', views.signup, name = 'signup'),
    path('newaccount/', views.newaccount, name = 'newaccount'),
    path('signin/', views.signin, name = 'signin'),
    path('userhome/', views.userhome, name='userhome'),
]
