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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CategoryMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def show_categories(request):
        return render_to_response("category_list.html",
                                  {'nodes': Category.objects.all()},
                                  context_instance=RequestContext(request))


class CategoryListView(CategoryMixin, ListView):
    pass


class CategoryCreateView(CategoryMixin, CreateView):
    pass


class CategoryDeleteView(CategoryMixin, DeleteView):
    pass


class CategoryUpdateView(CategoryMixin, UpdateView):
    pass
