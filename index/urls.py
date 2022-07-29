from . import views
from django.urls import path

urlpatterns = [
    path('Expert', views.ExpertAPI.as_view(), name='expert_api'),
]
