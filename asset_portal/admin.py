from django.contrib import admin

from models import *


# Register your models here.
from user_manager.models.accounting import Invoice

admin.site.register(Asset)

admin.site.register(Invoice)
admin.site.register(ShippingJob)
# admin.site.register(RequestLogoChangeJob)
admin.site.register(RequestQCCheckJob)
admin.site.register(OrderPhysicalDCPJob)
admin.site.register(MakeDCPJob)
admin.site.register(SendDCPJob)
admin.site.register(SendDVDJob)
admin.site.register(SendBlurayJob)

admin.site.register(EncodeDVDJob)
admin.site.register(EncodeBlurayJob)

admin.site.register(Flight)
