from django.urls import path
from . import views

urlpatterns = [
    path('dryClean', views.dryClean, name='dryClean'),
    path('dryClean/services/<int:id>', views.services, name='services'),
    path("dryClean/register", views.register, name="register"),
    path("dryClean/login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
