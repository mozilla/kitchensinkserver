"""
device.api
----------
"""
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from kitchensink.device.models import Make, Device


class MakeResource(ModelResource):
    class Meta:
        queryset = Make.objects.all()
        # read only until we decide the other way
        allowed_methods = ('get',)
        always_return_data = True
        filtering = {
            'slug': ALL
        }


class DeviceResource(ModelResource):
    make = fields.ForeignKey(MakeResource, 'make', full=True)

    class Meta:
        queryset = Device.objects.all()
        # read only until we decide the other way
        allowed_methods = ('get',)
        always_return_data = True
        filtering = {
            'make': ALL_WITH_RELATIONS,
            'model': ALL
        }
