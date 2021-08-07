from rest_framework import routers
from product.api.views import *
from register.api.views import *
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
# router.register('auth', UsersViewSet, basename="auth-view-set")
# router.register('profile', ProfileViewSet, basename="profile-view-set")
router.register('products', ProductViewSet, basename="product-view-set")
router.register('categorys', CategoryViewSet, basename="category-view-set")
router.register('services', ServiceViewSet, basename="service-view-set")
router.register('sizes', SizeViewSet, basename="size-view-set")


urlpatterns = [
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterViewSet.as_view()),
    path('users/', UsersViewSet.as_view()),
    path('users/<pk>/', UserDetailViewSet.as_view()),
    path('detail/', ProfileViewSet.as_view()),
]

urlpatterns += router.urls
