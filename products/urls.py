from django.urls import path, re_path
from . import views

# link for dynamic editing: https://stackoverflow.com/questions/56614040/how-can-i-generate-a-page-dynamically-in-django

urlpatterns = [
    path('', views.index),
    path('products/', views.index, name='products'),
    path('info/<int:pk>/', views.info, name='info'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('info/<int:pk>/add-comment', views.add_comment, name='add-comment'),
    path('payment-status', views.payment_status, name='payment-status'),


]
