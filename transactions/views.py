import json

from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import QueryDict, HttpResponse
from django.views.generic import CreateView, UpdateView
from django_ajax.decorators import ajax
from endless_pagination.views import AjaxListView

from transactions.forms import TransactionForm
from transactions.models import Transaction


class TransactionMixin(LoginRequiredMixin):
    model = Transaction
    form_class = TransactionForm

    def get_success_url(self):
        return reverse('transaction_list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

        # def form_valid(self, form):
        # self.object = form.save(commit=False)
        # self.object.user = self.request.user
        # self.object.save()
        # return super(LoginRequiredMixin, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(TransactionMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TransactionListView(TransactionMixin, AjaxListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        type_ = self.request.GET.get('type')
        if type_ == 'incoming':
            queryset = queryset.filter(account_from=None)
        elif type_ == 'outgoing':
            queryset = queryset.filter(account_to=None)
        elif type_ == 'transfer':
            queryset = queryset.filter(account_to__isnull=False, account_from__isnull=False)
        return queryset


class TransactionCreateView(TransactionMixin, CreateView):
    pass


class TransactionDeleteView():
    @login_required
    @ajax
    def delete_transaction(request):
        transaction = Transaction.objects.get(pk=int(QueryDict(request.body).get('pk')))
        if transaction.user == request.user:
            transaction.delete()
            return HttpResponse(
                json.dumps({'msg': 'Transaction was deleted.'}),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"msg": "Transaction was not deleted"}),
                content_type="application/json"
            )


class TransactionUpdateView(TransactionMixin, UpdateView):
    pass
