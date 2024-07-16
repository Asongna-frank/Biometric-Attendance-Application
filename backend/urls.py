from django.contrib import admin
from django.urls import path, include
from users.custom_admin import custom_admin_site
from api.viewsets.usersViewsets import PublicView, ProtectedView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path("api/", include("api.routes")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
    path('api/public/', PublicView.as_view(), name='public_view'),

]
