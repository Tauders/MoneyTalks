# Create your views here.
import json

from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import QueryDict, HttpResponse
from django.views.generic import CreateView, UpdateView
from django_ajax.decorators import ajax
from endless_pagination.views import AjaxListView

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


class AccountListView(AccountMixin, AjaxListView):
    pass


class AccountCreateView(AccountMixin, CreateView):
    pass


class AccountDeleteView():
    @login_required
    @ajax
    def delete_account(request):
        place = Account.objects.get(pk=int(QueryDict(request.body).get('pk')))
        if place.user == request.user:
            place.delete()
            return HttpResponse(
                json.dumps({'msg': 'Account was deleted.'}),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({'msg': 'Account was not deleted.'}),
                content_type="application/json"
            )


class AccountUpdateView(AccountMixin, UpdateView):
    pass
