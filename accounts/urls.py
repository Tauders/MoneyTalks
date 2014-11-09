from django.conf.urls import patterns, url

from accounts.views import AccountListView, AccountCreateView, AccountUpdateView, AccountDeleteView


urlpatterns = patterns('',
                       url(
                           regex=r'^$',
                           view=AccountListView.as_view(),
                           name='account_list'
                       ),
                       url(
                           regex=r'^create/$',
                           view=AccountCreateView.as_view(),
                           name='account_create'
                       ),
                       url(
                           regex=r'^delete/(?P<pk>\d+)/$',
                           view=AccountDeleteView.as_view(),
                           name='account_delete'
                       ),
                       url(
                           regex=r'^update/(?P<pk>\d+)/$',
                           view=AccountUpdateView.as_view(),
                           name='account_update'
                       ), )
