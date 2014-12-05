# Create your views here.
import json

from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.http import QueryDict, HttpResponse
from django_ajax.decorators import ajax
from django.contrib.auth.decorators import login_required

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


class CategoryDeleteView():
    @login_required
    @ajax
    def delete_category(request):
        category = Category.objects.get(pk=int(QueryDict(request.body).get('pk')))
        if category.user == request.user:
            category.delete()
            return HttpResponse(
                json.dumps({'msg': 'Category was deleted.'}),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"msg": "Category was not deleted."}),
                content_type="application/json"
            )


class CategoryUpdateView(CategoryMixin, UpdateView):
    pass
