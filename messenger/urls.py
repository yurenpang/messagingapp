from django.conf.urls import re_path
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='messenger/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^message_write/$', views.message_write, name='message_write'),
    re_path(r'^message_received/$', views.message_received, name='message_received'),
    re_path(r'^message_sent/$', views.message_sent, name='message_sent'),
    re_path(r'^message_draft/$', views.message_draft, name='message_draft'),
    # re_path(r'^message_edit/$', views.message_edit, name='message_edit'),

    path('edit/<int:pk>/', views.edit, name='edit')
]