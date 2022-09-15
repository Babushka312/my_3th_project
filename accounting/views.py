from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.parsers import JSONParser

from market.models import Product, Category
from market.serializers import ProductSerializer, CategorySerializer
from user.serializers import User


class PostLenApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]
    #
    # def get_object(self, price):
    #     try:
    #         return Product.objects.get(price=price)
    #     except Product.DoesNotExist:
    #         raise Http404

    def get(self, request):
        products = Product.objects.all()
        list = []
        list2 = []
        list3 = []
        list4 = []
        for p in products:
            list.append(p.price)
            list2.append(p.name)
            list3.append(p.quantity)
        price = sum(list) / len(list)
        price2 = min(list)
        price3 = max(list)
        price4 = len(list2)
        price5 = sum(list3)
        for i in products:
            one = i.price * i.quantity
            list4.append(one)
        price6 = sum(list4)

        data = {
            "Средняя сумма": price,
            "Минимальная сумма": price2,
            "Максимальная сумма": price3,
            "кол-во продуктов": price4,
            "Обший кол-во всех продуктов": price5,
            "Общая сумма всех продуктов": price6,
        }
        return Response(data)



class ProductFilterApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name', 'price']


class PriceApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, price):
        products = Product.objects.filter(price=price)
        serializer = ProductSerializer(products, many=True)
        data = serializer.data
        return Response(data)

    def get_object(self, price):
        try:
            return Product.objects.get(price=price)
        except Product.DoesNotExist:
            raise Http404


class CategoryApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name):
        category = self.get_object(name)
        products = Product.objects.filter(category__name=name)
        serializer = CategorySerializer(category)
        serializer2 = ProductSerializer(products, many=True)
        data = serializer.data
        data['products'] = serializer2.data

        return Response(data)



class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        user_list = []
        user_list2 = []
        for i in users:
            user_list.append(i.username)
            user_list2.append(i.email)

        username = user_list
        email = user_list2

        data = {
            "Пользователи": username,
            "Email Пользователей": email,
            "Кол-Во Пользователей": len(username)
        }
        return Response(data)