from django.shortcuts import get_object_or_404, render
# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import CategoryGroup

def index(request):
    category_groups_list = CategoryGroup.objects.all()
    context = {'category_groups_list': category_groups_list}
    return render(request, 'script/index.html', context)

def details(request, category_id):
    category_group = get_object_or_404(CategoryGroup, pk=category_id)
    return render(request, 'script/detail.html', {'category_group': category_group})
