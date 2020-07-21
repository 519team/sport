from django.urls import path
from .views import *

urlpatterns=[
	path('',site_lists, name='home_page'),
	path('shop/category/<int:index_cat>/', category_detail, name='cat_url'),
	path('shop/item/<int:index_item>/', item_detail, name='item_url')
]