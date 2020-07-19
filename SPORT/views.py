from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


def site_lists(request):
	return render(request,'base.html')

def category_detail(request, index_cat):
	categorys=Category.objects.all()
	return render(request, 'base.html', context={'categorys': categorys})