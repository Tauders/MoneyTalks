# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin

from places.forms import PlaceForm
from places.models import Place


class PlaceMixin(LoginRequiredMixin):
    model = Place
    form_class = PlaceForm

    def get_success_url(self):
        return reverse('place_list')

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


class PlaceListView(PlaceMixin, ListView):
    pass


class PlaceCreateView(PlaceMixin, CreateView):
    pass


class PlaceDeleteView(PlaceMixin, DeleteView):
    pass


class PlaceUpdateView(PlaceMixin, UpdateView):
    pass