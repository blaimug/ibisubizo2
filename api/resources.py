# api/resources.py

from tastypie.resources import ModelResource
from api.models import users

class UsersResource(ModelResource):
    class Meta:
        queryset = users.objects.all()
        resource_name = 'users'