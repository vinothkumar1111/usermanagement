from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('users/', views.users, name='users'),
    path('new_user/', views.new_user, name='new_user'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
    # path('users/<int:id>/delete/', views.delete_user, name='delete_user'),

]
# 