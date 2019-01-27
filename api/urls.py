from django.conf.urls import url, include
from . import views
from api.resources import CustomerResource
from api.resources import ItemResource
customer_resource = CustomerResource()
item_resource = ItemResource()


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^customer/', include(customer_resource.urls)),
    url('r^item/', include(item_resource.urls)),
]