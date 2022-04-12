from django.urls import path

from base.views import user_views as views
urlpatterns = [
  path('login', views.login_view, name='login'),
]
