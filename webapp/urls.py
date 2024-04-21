from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name=""),
    path('test/', views.test_view),
    path('base/', views.base_view),
    path('login/', views.login_view, name="login"),
    path('dashboard', views.dashboard_view, name="dashboard"),
]
