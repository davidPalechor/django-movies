from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


app_name = 'user'
urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
