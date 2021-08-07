from rest_framework import viewsets
from .serializers import *
from .filtersSet import *
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from register.models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.http import JsonResponse
from urllib.parse import urlparse
import urllib.request as urllib2
import io



class RegisterViewSet(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes=[AllowAny]
    user = None
    profile = None
    def post(self, request, *args,  **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        profile = Profile.objects.create(user=user, phone_number=request.data.get("phoneNumber"))
        # img_url = request.data.get("image")
        # name_image = urlparse(img_url).path.split('/')[-1]
        # content = io.BytesIO(urllib2.urlopen(img_url).read())
        # profile.image.save(name_image, content, save=True)
        profile.save()
        return JsonResponse({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
        

class UsersViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =["id","username"]

class UserDetailViewSet(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes=[IsAuthenticated,]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =["id","username"]

class ProfileViewSet(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    permission_classes=[IsAuthenticated,]
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =["id","user"]





