from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import *
from .forms import *
from .utils import *
from .serializers import *
from .permissions import *

menu = [{'title': 'Войти', 'url_name': 'login'},
        {'title': 'Профиль', 'url_name': 'profile'},
        {'title': 'Уведомления', 'url_name': 'notifications'},
        {'title': 'Корзина', 'url_name': 'cart'},
        ]


# {'title': 'Смартфоны', 'url_name': 'smartphones'},
# {'title': 'Ноутбуки', 'url_name': 'notebooks'},
# {'title': 'Телевизоры', 'url_name': 'TVs'},
# {'title': 'Книги', 'url_name': 'books'},
# {'title': 'Одежда', 'url_name': 'clothes'},
# {'title': 'Скидки', 'url_name': 'sales'},
# ]
#

# Outputs all items
class ItemAPIList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)


# Outputs all categories
class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


# Outputs items through slug
class ItemAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSlugSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'


# Outputs categories through slug
class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = ItemsInCatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'


# destroy item or category
class ItemAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)

# class MainPage(DataMixin, ListView):
#     model = Category
#     template_name = 'main/index.html'
#     context_object_name = 'categories'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Главная страница')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_queryset(self):
#         return Category.objects.filter(availability=True).selected_related('cat')
#
#
# class ItemsPage(DataMixin, ListView):
#     model = Item
#     template_name = 'main/items.html'
#     context_object_name = 'items'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Страница категории')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_queryset(self):
#         return Category.objects.filter(is_published=True).selected_related('cat')
#
