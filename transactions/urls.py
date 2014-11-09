from django.conf.urls import patterns, url

from transactions.views import TransactionListView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView


urlpatterns = patterns('transactions.views',
                       url(
                           regex=r'^$',
                           view=TransactionListView.as_view(),
                           name='transaction_list'
                       ),
                       url(
                           regex=r'^create/$',
                           view=TransactionCreateView.as_view(),
                           name='transaction_create'
                       ),
                       url(
                           regex=r'^delete/$',
                           view=TransactionDeleteView.delete_transaction,
                           name='transaction_delete'
                       ),
                       url(
                           regex=r'^update/(?P<pk>\d+)/$',
                           view=TransactionUpdateView.as_view(),
                           name='transaction_update'
                       ), )
