from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect, get_object_or_404

from .models import Recipe
from .forms import RecipeForm, RecipeImageUploadForm


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"

class RecipeUploadImageView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeImageUploadForm
    template_name = "recipe_upload.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})
    
    def post(self, request, *args, **kwargs):
        form = RecipeImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.recipe_id = self.kwargs['pk']
            form.save()
        return redirect(self.get_success_url())