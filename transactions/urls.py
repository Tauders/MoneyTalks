from django.conf.urls import patterns, include, url
from django.contrib import admin
from transactions.views import TransactionList

urlpatterns = patterns('',
    url(
        r'^$', TransactionList.as_view(),
        name='transaction_list'
    ),
)

