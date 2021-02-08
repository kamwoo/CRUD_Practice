from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

# accounts/profile/
# 1. profile 만들기
# 2. profile 페이지가 아닌 페이지로 보내기(장고 설정변경, 웹서버에서 설정(redirect))
urlpatterns =[
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
]