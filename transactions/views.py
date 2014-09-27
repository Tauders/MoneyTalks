from django.shortcuts import render
from django.views.generic import ListView
from transactions.models import Transaction


class TransactionList(ListView):
    model = Transaction
