"""userserviceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', views.get_all_users, name='get_all_users'),
    path('users/<int:user_id>', views.get_user_by_id, name='get_user_by_id'),
    path('signup/user', views.create_user, name='create_user'),
    path('signin', views.sign_in_user, name='sign_in_user'),
    path('users/<int:user_id>/update', views.update_user, name='update_user'),
    path('users/change-password', views.change_password, name='change_password'),
    path('users/<int:user_id>/delete', views.delete_user_by_id, name='delete_user_by_id'),
    path('users/delete-all', views.delete_all_users, name='delete_all_users'),
    path('users/email/<str:email>', views.get_user_by_email, name='get_user_by_email')
]
