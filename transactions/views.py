import json
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import QueryDict, HttpResponse
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(LoginRequiredMixin, self).form_valid(form)


class TransactionListView(TransactionMixin, AjaxListView):
    pass


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