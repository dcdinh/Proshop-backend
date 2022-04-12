from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from base.views import user_views as views
urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view()),
    path('register', views.register_user),
    path('profile', views.get_user_profile),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]