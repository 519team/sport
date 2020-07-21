from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .models import Item

def site_lists(request):
	categorys=Category.objects.all()
	return render(request,'base.html', context={'categorys': categorys})

def category_detail(request, index_cat):
	Categorys=Category.objects.all()
	category=Category.objects.get(index_cat=index_cat)
	items=Item.objects.filter(id_category=category.id)
	return render(request, 'SPORT/category.html', context={'category': category, 'items': items, 'categorys': Categorys})

def item_detail(request, index_item):
	categorys=Category.objects.all()
	return render(request, 'SPORT/item.html', context={'categorys': categorys})