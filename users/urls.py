from django.urls import path
from .views import RegisterApi, MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('apilogin/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
