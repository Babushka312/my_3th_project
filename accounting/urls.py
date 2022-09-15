from django.urls import path
from .views import (
    CategoryApiView,
    PriceApiView,
    PostLenApiView, ProductFilterApiView, UserListView
)

urlpatterns = [
        path('filter/<slug:name>/', CategoryApiView.as_view(), name='filter_category'),
        path('user_list/', UserListView.as_view(), name='user-list'),
        path('filter/price/<slug:price>/', PriceApiView.as_view(), name='filter_price'),
        path('filter_product/', ProductFilterApiView.as_view(), name='filter-product'),
        path('product/', PostLenApiView.as_view(), name='buh'),
    ]