# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin

from categories.forms import CategoryForm
from categories.models import Category


class CategoryMixin(LoginRequiredMixin):
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('category_list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CategoryMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CategoryListView(CategoryMixin, ListView):
    pass


class CategoryCreateView(CategoryMixin, CreateView):
    pass


class CategoryDeleteView(CategoryMixin, DeleteView):
    pass


class CategoryUpdateView(CategoryMixin, UpdateView):
    pass