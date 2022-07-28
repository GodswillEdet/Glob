from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('login/', views.login_request, name='login'),
]
