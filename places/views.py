# Create your views here.
from django.views.generic import DeleteView, ListView, CreateView, UpdateView

from places.models import PlaceMixin


class PlaceListView(PlaceMixin, ListView):
  pass


class PlaceCreateView(PlaceMixin, CreateView):
  pass


class PlaceDeleteView(PlaceMixin, DeleteView):
  pass


class PlaceUpdateView(PlaceMixin, UpdateView):
  pass