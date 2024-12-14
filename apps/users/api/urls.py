from django.urls import path
from .views.register_user_view import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    # Add other routes
]
