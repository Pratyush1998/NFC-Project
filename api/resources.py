from tastypie.resources import ModelResource
from api.models import Customer
from tastypie.authorization import Authorization
class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'
        authorization = Authorization()