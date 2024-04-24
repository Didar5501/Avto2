from django.urls import path, include
from account import views

urlpatterns = [
    path("register/", views.RegisterAccApi.as_view(), name='register'),
    path('update/<int:id>/', views.UpdateUserApi.as_view(), name='update-user'),
    path('delete_user/<int:pk>/', views.UserDeleteAPIView.as_view(), name='user-delete'),
    path('detail/<int:id>/', views.AccountDetailApi.as_view(), name='detail-user'),

]