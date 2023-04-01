from .models import *
from django.db.models import Count

menu = [{'title': 'Профиль', 'url_name': 'profile'},
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

class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
            user_menu.pop(0)
        context['menu'] = user_menu
        return context
