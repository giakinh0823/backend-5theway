from rest_framework import viewsets
from .serializers import *
from .filtersSet import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.models import User
from register.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication





class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    # permission_classes=[IsAuthenticated,]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =["id","username"]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes=[IsAuthenticated,]
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =["id","user"]





