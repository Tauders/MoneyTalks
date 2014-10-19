from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.core.exceptions import ValidationError

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
        return super(ModelFormMixin, self).form_valid(form)


class TransactionListView(TransactionMixin, ListView):
    pass


class TransactionCreateView(TransactionMixin, CreateView):
    pass


class TransactionDeleteView(TransactionMixin, DeleteView):
    pass


class TransactionUpdateView(TransactionMixin, UpdateView):
    pass