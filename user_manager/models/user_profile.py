from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=200)
    ORG_TYPE_CHOICES = (
        ('RESELLER', 'Reseller'),
        ('DIST', 'Distributor'),
    )
    type = models.CharField(choices=ORG_TYPE_CHOICES, max_length=50)
    credit = models.DecimalField(max_digits=20, decimal_places=2)


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name="profile")
    title = models.CharField(max_length=20, blank=True)
    org = models.ForeignKey(Organization, blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return "%s's profile" % self.user.username


class CreditCard(models.Model):
    user = models.ForeignKey('auth.User', related_name="creditcards")
    card_id = models.CharField(max_length=50)
    fingerprint = models.CharField(max_length=50)


# automatically make a user profile when a user is created
def create_user_profile(sender, **kwargs):
    """When creating a new user, make a profile for him or her."""
    created = kwargs["created"]
    if created:
        u = kwargs["instance"]
        if not UserProfile.objects.filter(user=u):
            user_profile = UserProfile(user=u)
            user_profile.save()


post_save.connect(create_user_profile, sender=User)
