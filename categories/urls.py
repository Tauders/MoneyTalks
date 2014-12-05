from django.conf.urls import patterns, url

from categories.views import CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView


urlpatterns = patterns('',
                       url(
                           regex=r'^$',
                           view=CategoryListView.as_view(),
                           name='category_list'
                       ),
                       url(
                           regex=r'^create/$',
                           view=CategoryCreateView.as_view(),
                           name='category_create'
                       ),
                       url(
                           regex=r'^delete/$',
                           view=CategoryDeleteView.delete_category,
                           name='category_delete'
                       ),
                       url(
                           regex=r'^update/(?P<pk>\d+)/$',
                           view=CategoryUpdateView.as_view(),
                           name='category_update'
                       ))
