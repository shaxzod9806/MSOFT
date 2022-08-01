from . import views
from django.urls import path

urlpatterns = [
    path('Expert', views.ExpertAPI.as_view(), name='expert_api'),
    path('Title', views.TitleAPI.as_view(), name='title_api'),
    path('Sector', views.SectorApi.as_view(), name='sector_api'),
    path('Work_experience', views.Work_experienceApi.as_view(), name='work_experience_api'),
    path('Citezenship', views.CitezenshipApi.as_view(), name='citezenship_api'),
    path('Language', views.LanguageApi.as_view(), name='language_api'),

]
