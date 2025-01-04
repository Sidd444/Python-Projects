from django.urls import path
from user_auth import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_page', views.register, name='register_page'),
    path('login_page', views.login_view, name='login_page'),
    path('logout_page', views.logout_view, name='logout_page'),
]

