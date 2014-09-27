from django.conf.urls import patterns, url

from transactions.views import TransactionList


urlpatterns = patterns('',
                       url(
                         r'^$', TransactionList.as_view(),
                         name='transaction_list'
                       ),
)
