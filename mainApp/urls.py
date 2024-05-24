from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServicesListCreateAPIView.as_view()),
    path('services/<int:pk>/', ServicesRetrieveUpdateDestroyAPIView.as_view()),
    path('myTeams/', MyTeamListCreateAPIView.as_view()),
    path('myTeam/<int:pk>/', MyTeamRetrieveUpdateDestroyAPIView.as_view()),
    path('usAbouts/', UsAboutListCreateAPIView.as_view()),
    path('usAbout/<int:pk>/', UsAboutRetrieveUpdateDestroyAPIView.as_view()),
    path('registerTeams/', RegisterTeamListCreateAPIView.as_view()),
    path('registerTeam/<int:pk>/', RegisterTeamRetrieveUpdateDestroyAPIView.as_view()),
    path('partners/', PartnersListCreateAPIView.as_view()),
]
