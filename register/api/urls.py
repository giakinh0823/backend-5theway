from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('auth', UsersViewSet, basename="auth-view-set")
router.register('profile', ProfileViewSet, basename="profile-view-set")
urlpatterns = router.urls
