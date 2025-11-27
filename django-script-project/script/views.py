from django.shortcuts import get_object_or_404, render
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy
from .forms import ScriptForm, CategoryGroupForm

from .models import CategoryGroup, Script

def index(request):
    category_groups_list = CategoryGroup.objects.all()
    context = {'category_groups_list': category_groups_list}
    return render(request, 'script/index.html', context)

def details(request, category_id):
    category_group = get_object_or_404(CategoryGroup, pk=category_id)
    return render(request, 'script/detail.html', {'category_group': category_group})

class ScriptListView(ListView):
    model = Script
    template_name = 'templates/script/scriptList.html'

class ScriptDetailView(DetailView):
    model = Script
    template_name = "script/scriptDetail.html"

class ScriptCreateView(CreateView):
    model = Script
    form_class = ScriptForm
    template_name = 'script/scriptCreate.html'
    success_url = reverse_lazy('script:index')

def script_create(request):
    if request.method == 'POST':
        form = ScriptForm(request.POST)
        if form.is_valid():
            script = form.save()
            return redirect('script/scriptDetail.html', pk=script.pk)
    else:
        form = ScriptForm()

    return render(request, 'script/script_create.html', {'form': form})

class ScriptUpdateView(UpdateView):
    model = Script
    form_class = ScriptForm
    template_name = 'script/scriptCreate.html'
    success_url = reverse_lazy('script:index')

def script_edit(request, pk):
    script = get_object_or_404(Script, pk=pk)

    if request.method == 'POST':
        form = ScriptForm(request.POST, instance=script)
        if form.is_valid():
            form.save()
            return redirect('script/scriptDetail.html', pk=pk)
    else:
        form = ScriptForm(instance=script)

    return render(request, 'script_edit.html', {'form': form})

class ScriptDeleteView(DeleteView):
    model = Script
    form_class = ScriptForm
    template_name = 'script/scriptDelete.html'
    success_url = reverse_lazy('script/scriptList.html')

def script_delete(request, pk):
    script = get_object_or_404(Script, pk=pk)

    if request.method == 'POST':
        script.delete()
        return redirect('script_list')

    return render(request, 'script/scriptDelete.html', {'script': script})

class CategoryGroupListView(ListView):
    model = CategoryGroup
    template_name = "script/category_list.html"

class CategoryGroupCreateView(CreateView):
    model = CategoryGroup
    form_class = CategoryGroupForm
    template_name = "script/category_form.html"
    success_url = reverse_lazy('script:category_list')

def category_create(request):
    if request.method == 'POST':
        form = CategoryGroupForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('script/category_detail', pk=category.pk)
    else:
        form = CategoryGroupForm()

    return render(request, 'script/category_create.html', {'form': form})

class CategoryGroupUpdateView(UpdateView):
    model = CategoryGroup
    form_class = CategoryGroupForm
    template_name = "script/category_form.html"
    success_url = reverse_lazy('script:category_list')

def category_edit(request, pk):
    category = get_object_or_404(CategoryGroup, pk=pk)

    if request.method == 'POST':
        form = CategoryGroupForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('script/category_detail', pk=pk)
    else:
        form = CategoryGroupForm(instance=category)

    return render(request, 'script/category_edit.html', {'form': form})

class CategoryGroupDeleteView(DeleteView):
    model = CategoryGroup
    template_name = "script/category_confirm_delete.html"
    success_url = reverse_lazy('script:category_list')


def category_delete(request, pk):
    category = get_object_or_404(CategoryGroup, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(request, 'category_delete.html', {'category': category})

class ScriptByCategoryListView(ListView):
    model = Script
    template_name = "script/script_list.html"

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Script.objects.filter(CategoryGroup_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryGroup.objects.get(pk=self.kwargs['pk'])
        return context