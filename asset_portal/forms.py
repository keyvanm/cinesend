from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import ModelForm
from django_select2 import ModelSelect2MultipleField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django_select2.fields import Select2ChoiceField
from django_select2.widgets import Select2MultipleWidget
from asset_portal.models.job import EncodeDVDJob, EncodeBlurayJob

from user_manager.models.address import Address
from user_manager.models.exhibitor import ScreeningRoom
from models import Asset, RequestQCCheckJob, OrderPhysicalDCPJob, \
    MakeDCPJob, SendDCPJob, SendDVDJob
from asset_portal.models.vault_job import SendBlurayJob, SendDVDJob


class FixedModelForm(forms.ModelForm):
    """
    Simple child of ModelForm that removes the 'Hold down "Control" ...'
    message that is enforced in select multiple fields.

    See https://github.com/asyncee/django-easy-select2/issues/2
    and https://code.djangoproject.com/ticket/9321
    """

    def __init__(self, *args, **kwargs):
        super(FixedModelForm, self).__init__(*args, **kwargs)

        msg = force_text(_(' Hold down "Control", or "Command" on a Mac, to select more than one.'))

        for name, field in self.fields.items():
            field.help_text = field.help_text.replace(msg, '')


class AssetForm(FixedModelForm):
    # owners = ModelSelect2MultipleField(queryset=User.objects, required=False)
    audio_language = Select2ChoiceField(choices=Asset.AUDIO_LANG_CHOICES)
    subtitle_language = Select2ChoiceField(choices=Asset.SUBTITLE_LANG_CHOICES)
    territory = Select2ChoiceField(choices=Asset.TERRITORY_CHOICES)
    rating = Select2ChoiceField(choices=Asset.RATING_CHOICES)

    class Meta:
        model = Asset
        exclude = ['owners', 'made_by', 'deleted', 'status', 'running_time', 'file_type', 'is_title_safe']


# class RequestLogoChangeJobForm(ModelForm):
# logos = ModelSelect2MultipleField(queryset=Logo.objects, required=False)
#
#
# class Meta:
# model = RequestLogoChangeJob
# fields = ['version_name', 'logos']


class RequestQCCheckJobForm(ModelForm):
    class Meta:
        model = RequestQCCheckJob
        fields = []


class OrderPhysicalDCPJobForm(ModelForm):
    class Meta:
        model = OrderPhysicalDCPJob
        fields = ['two_d_to_3d', 'four_k_to_2K_scaling', 'foureight_fps_to_twofour_fps', 'audio_adjustment_to_85dBs',
                  'create_encrypted_dcp', 'number_of_copies']


class MakeDCPJobForm(ModelForm):
    class Meta:
        model = MakeDCPJob
        # fields = ['two_d_to_3d', 'four_k_to_2K_scaling', 'foureight_fps_to_twofour_fps', 'audio_adjustment_to_85dBs', ]
        fields = ['number_of_copies']


class SendDCPJobForm(ModelForm):
    addresses = ModelSelect2MultipleField(queryset=ScreeningRoom.objects, required=True)
    screening_start_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    screening_end_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))

    class Meta:
        model = SendDCPJob
        fields = ['addresses', 'screening_start_date', 'screening_end_date']


class EncodeDVDJobForm(FixedModelForm):
    class Meta:
        model = EncodeDVDJob
        fields = ['video_format']

class SendDVDJobForm(FixedModelForm):
    addresses = ModelSelect2MultipleField(queryset=Address.objects,
                                          widget=Select2MultipleWidget(select2_options={'width': '100%'}))

    class Meta:
        model = SendDVDJob
        fields = ['addresses', ]


class EncodeBlurayJobForm(FixedModelForm):
    class Meta:
        model = EncodeBlurayJob
        fields = []

class SendBlurayJobForm(FixedModelForm):
    addresses = ModelSelect2MultipleField(queryset=Address.objects,
                                          widget=Select2MultipleWidget(select2_options={'width': '100%'}))

    class Meta:
        model = SendBlurayJob
        fields = ['addresses', ]
