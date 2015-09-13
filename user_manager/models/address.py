from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from model_utils.choices import Choices


class Address(TimeStampedModel):
    user = models.ForeignKey(User, null=True, blank=True, related_name='personal_addresses')

    TYPE_CHOICES = Choices('billing', 'shipping')  # billing addresses must be private
    type = models.CharField(choices=TYPE_CHOICES, default=TYPE_CHOICES.shipping, max_length=20)
    PRIVACY_CHOICES = Choices(('private', 'Private'), ('pending', 'Pending Approval'), ('public', 'Public'))  # billing addresses must be private
    privacy = models.CharField(choices=PRIVACY_CHOICES, default=PRIVACY_CHOICES.private, max_length=20)
    primary = models.BooleanField(default=False)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    address1 = models.CharField(max_length=255, verbose_name="Street Address")
    address2 = models.CharField(max_length=255, blank=True, verbose_name="Apt/Suite/Bldg")
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, verbose_name='State/Province')
    postal_code = models.CharField(max_length=20, verbose_name="ZIP/Postal Code")
    country = models.CharField(max_length=200)

    def __unicode__(self):
        if self.address2:
            return "{} - {}, {}, {} {}, {}".format(
                self.address2, self.address1, self.city, self.state, self.postal_code.upper(), self.country)
        return "{}, {}, {} {}, {}".format(self.address1, self.city, self.state, self.postal_code.upper(), self.country)

    def clean(self):
        if self.type == self.TYPE_CHOICES.billing and self.privacy == self.PRIVACY_CHOICES.public:
            raise ValidationError('Billing addresses cannot be public')

    class Meta:
        verbose_name_plural = "addresses"
