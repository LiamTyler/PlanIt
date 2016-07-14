from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/', views.login_page, name="login"),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^sign_up/', views.sign_up, name="sign_up"),
    url(r'^profile/', views.profile, name="profile"),
]
