from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django.utils.decorators import method_decorator
from django.views.generic.edit import ModelFormMixin


class Place(models.Model):
  name = models.CharField(max_length=80)
  user = models.ForeignKey(User, related_name='places')

  def __str__(self):
    return self.name


class LoginRequiredMixin(object):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class PlaceForm(ModelForm):
  class Meta:
    model = Place
    exclude = ('user',)


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


