# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin

from accounts.forms import AccountForm
from accounts.models import Account


class AccountMixin(LoginRequiredMixin):
    model = Account
    form_class = AccountForm

    def get_success_url(self):
        return reverse('account_list')

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


class AccountListView(AccountMixin, ListView):
    pass


class AccountCreateView(AccountMixin, CreateView):
    pass


class AccountDeleteView(AccountMixin, DeleteView):
    pass


class AccountUpdateView(AccountMixin, UpdateView):
    pass