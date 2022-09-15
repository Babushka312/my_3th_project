from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from user.permissions import AnonPermissionOnly
from .models import Product, Category
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework import permissions, status, generics
from .serializers import CategorySerializer
from user.serializers import User
# from .serializers import ProductPriceSerializer


class ProductListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,  request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page_num = self.request.query_params.get('page')
        print(page_num)
        serializers = ProductSerializer(paginator.page(page_num), many=True)
        return Response(serializers.data)


class ProductCreateApiView(APIView):

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializers = ProductSerializer(post)
        data = serializers.data
        return Response(data)


class ProductUpdateApiView(APIView):
    # permission_classes = [permissions.AllowAny]

    # def get_object(self, id):
    #     try:
    #         return Product.objects.get(id=id)
    #     except Product.DoesNotExist:
    #         raise Http404

    def put(self, requests,id):
        post = self.get_object(id)
        serializer = ProductSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDestroyApiView(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListApiView(APIView):
    def get(self, request):
        products = Category.objects.all()
        serializers = CategorySerializer(products, many=True)
        return Response(serializers.data)


class CategoryCreateApiView(APIView):

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
