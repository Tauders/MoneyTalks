from django.conf.urls import patterns, url

from places.views import PlaceListView, PlaceCreateView, PlaceUpdateView, PlaceDeleteView


urlpatterns = patterns('places.views',
                       url(
                           regex=r'^$',
                           view=PlaceListView.as_view(),
                           name='place_list'
                       ),
                       url(
                           regex=r'^create/$',
                           view=PlaceCreateView.as_view(),
                           name='place_create'
                       ),
                       url(
                           regex=r'^delete/$',
                           view=PlaceDeleteView.delete_place,
                           name='place_delete'
                       ),
                       url(
                           regex=r'^update/(?P<pk>\d+)/$',
                           view=PlaceUpdateView.as_view(),
                           name='place_update'
                       ), )
