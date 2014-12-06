from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

from accounts.models import Account
from categories.models import Category
from places.models import Place
from transactions.models import Transaction


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['date_joined', 'email', 'id', 'last_login', 'username']
        allowed_methods = ['get']


class AccountResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Account.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }


class CategoryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Category.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }


class PlaceResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Place.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }


class TransactionResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Transaction.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
