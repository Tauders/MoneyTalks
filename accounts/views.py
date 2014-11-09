# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView, ListView, CreateView, UpdateView

from accounts.forms import AccountForm
from accounts.models import Account


class AccountMixin(LoginRequiredMixin):
    model = Account
    form_class = AccountForm

    def get_success_url(self):
        return reverse('account_list')

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(AccountMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AccountListView(AccountMixin, ListView):
    pass


class AccountCreateView(AccountMixin, CreateView):
    pass


class AccountDeleteView(AccountMixin, DeleteView):
    pass


class AccountUpdateView(AccountMixin, UpdateView):
    pass
