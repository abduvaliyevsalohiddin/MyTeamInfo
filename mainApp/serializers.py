from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class MyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTeam
        fields = '__all__'


class UsAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsAbout
        fields = '__all__'


class RegisterTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterTeam
        fields = '__all__'


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'
