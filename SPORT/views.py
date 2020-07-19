from django.shortcuts import render
from django.http import HttpResponse


def site_lists(request):
	return render(request,'base.html')

def category_detail(request, index_cat):
	category=Category.objects.get(index_cat__iexact=index_cat)
	return render(request, 'SPORT/category.html', context={'category': category})