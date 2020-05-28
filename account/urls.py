
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='twitterclone/logout.html'), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='twitterclone/login.html'), name="login"),
]
