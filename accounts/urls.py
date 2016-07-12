from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/', views.login_page, name="login"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^auth_user/', views.auth_user, name="auth_user"),
    url(r'^sign_up/', views.sign_up, name="sign_up"),
    url(r'^create_user/', views.create_user, name="create_user"),
    url(r'^profile/', views.profile, name="profile"),
]
