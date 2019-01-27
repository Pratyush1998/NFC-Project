from tastypie.resources import ModelResource
from api.models import Customer
from api.models import Items
from tastypie.authorization import Authorization
class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'
        authorization = Authorization()

#class ItemResource(ModelResource):
 #   class Meta:
  #      queryset = Items.objects.all()
   #     resource_name = 'item'
    #    authorization = Authorization()