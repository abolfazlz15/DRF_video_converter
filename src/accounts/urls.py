from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
app_name = 'accounts'
urlpatterns = [
    # JWT URL
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]