from django.shortcuts import render_to_response
from categories.models import Category, SubCategory

def categories_menu(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return render_to_response('categories_menu.html', {'categories':categories, 'subcategories':subcategories})
