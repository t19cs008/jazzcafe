from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signedup/', views.SignedupView.as_view(), name='signedup')
]