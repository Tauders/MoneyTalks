from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import Unauthorized

from accounts.models import Account
from categories.models import Category
from places.models import Place
from transactions.models import Transaction


class UserObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.user == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming they're auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['date_joined', 'email', 'id', 'last_login', 'username']
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class AccountResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Account.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class CategoryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Category.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class PlaceResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Place.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class TransactionResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Transaction.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()
