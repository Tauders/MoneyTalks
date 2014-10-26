# Create your views here.
import json

from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import QueryDict, HttpResponse
from django.views.generic import CreateView, UpdateView
from django_ajax.decorators import ajax
from endless_pagination.views import AjaxListView

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
        return super(LoginRequiredMixin, self).form_valid(form)


class PlaceListView(PlaceMixin, AjaxListView):
    pass


class PlaceCreateView(PlaceMixin, CreateView):
    pass


class PlaceDeleteView():
    @login_required
    @ajax
    def delete_place(request):
        place = Place.objects.get(pk=int(QueryDict(request.body).get('pk')))
        if place.user == request.user:
            place.delete()
            return HttpResponse(
                json.dumps({'msg': 'Place was deleted.'}),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"msg": "Place was not deleted."}),
                content_type="application/json"
            )


class PlaceUpdateView(PlaceMixin, UpdateView):
    pass