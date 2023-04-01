from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .forms import *
from .utils import *

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

class MainPage(DataMixin, ListView):
    model = Category
    template_name = 'main/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Category.objects.filter(availability=True).selected_related('cat')


class ItemsPage(DataMixin, ListView):
    model = Item
    template_name = 'main/items.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Страница категории')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Category.objects.filter(is_published=True).selected_related('cat')

