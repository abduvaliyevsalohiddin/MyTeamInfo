from rest_framework.generics import *

from .serializers import *


class ServicesListCreateAPIView(ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class ServicesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class MyTeamListCreateAPIView(ListCreateAPIView):
    queryset = MyTeam.objects.all()
    serializer_class = MyTeamSerializer


class MyTeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyTeam.objects.all()
    serializer_class = MyTeamSerializer


class UsAboutListCreateAPIView(ListCreateAPIView):
    queryset = UsAbout.objects.all()
    serializer_class = UsAboutSerializer


class UsAboutRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UsAbout.objects.all()
    serializer_class = UsAboutSerializer


class RegisterTeamListCreateAPIView(ListCreateAPIView):
    queryset = RegisterTeam.objects.all()
    serializer_class = RegisterTeamSerializer


class RegisterTeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = RegisterTeam.objects.all()
    serializer_class = RegisterTeamSerializer
