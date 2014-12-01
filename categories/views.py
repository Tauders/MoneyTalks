# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render_to_response

from categories.forms import CategoryForm
from categories.models import Category


class CategoryMixin(LoginRequiredMixin):
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('category_list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(CategoryMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CategoryListView(CategoryMixin, ListView):
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user, parent=None)


class CategoryCreateView(CategoryMixin, CreateView):
    pass


class CategoryDeleteView(CategoryMixin, DeleteView):
    pass


class CategoryUpdateView(CategoryMixin, UpdateView):
    pass
