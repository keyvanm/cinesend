from django.db import models
from django_extensions.db.models import TimeStampedModel

from user_manager.models.address import Address
from user_manager.models.user_profile import Organization


class Festival(TimeStampedModel):
    name = models.CharField(max_length=200)
    location = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    submission_address = models.OneToOneField(Address,
                                              related_name='festival_submission')  # The address needs to be a global, shipping address.
    print_traffic_address = models.OneToOneField(Address,
                                                 related_name='festival_print_traffic')  # The address needs to be a global, shipping address.
    organization = models.ForeignKey(Organization, null=True, blank=True)
