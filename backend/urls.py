from django.contrib import admin
from django.urls import path, include
from users.custom_admin import custom_admin_site
from users.views import ObtainTokenPairWithEmailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path("api/", include("api.routes")),
    path('api/token/', ObtainTokenPairWithEmailView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
