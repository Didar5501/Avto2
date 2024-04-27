from django.urls import path, include
from account import views

urlpatterns = [
    path("register/", views.RegisterAccAPIView.as_view(), name='register'),
    
    path('user_detail/<int:id>/', views.AccountDetailApi.as_view(), name='detail-user'),

    path('user_list/', views.UserListAPIView.as_view(), name='user-list'),
    

]