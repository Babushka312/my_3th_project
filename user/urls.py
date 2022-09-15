from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from user.views import (
    RegisterView,
    MyObtainPairView,
    UserListView,
    UserDetailApi
)


urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='list'),
    path('user_detail/<int:id>/', UserDetailApi.as_view(), name='user-detail'),
]
