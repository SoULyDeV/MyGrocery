from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
