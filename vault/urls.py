from django.conf.urls import patterns, url
from asset_portal.views.job import JobCreateSendDCPView, JobCreateSendDVDView, JobCreateSendBlurayView
from vault.views.dcp import DCPDetailView, DCPDeleteView
from vault.views.optical_disc import DVDDetailView, DVDDeleteView, BlurayDetailView, BlurayDeleteView

urlpatterns = patterns('asset_portal.views',
    url(r'^dcps/(?P<slug>[-_\w]+)/$', DCPDetailView.as_view(), name='dcp-detail'),
    url(r'^dcps/(?P<slug>[-_\w]+)/delete/$', DCPDeleteView.as_view(), name='dcp-delete'),

    url(r'^dvds/(?P<slug>[-_\w]+)/$', DVDDetailView.as_view(), name='dvd-detail'),
    url(r'^dvds/(?P<slug>[-_\w]+)/delete/$', DVDDeleteView.as_view(), name='dvd-delete'),

    url(r'^blurays/(?P<slug>[-_\w]+)/$', BlurayDetailView.as_view(), name='bluray-detail'),
    url(r'^blurays/(?P<slug>[-_\w]+)/delete/$', BlurayDeleteView.as_view(), name='bluray-delete'),

    url(r'^dcps/(?P<slug>[-_\w]+)/add-senddcp/$', JobCreateSendDCPView.as_view(),
        name='job-create-senddcp'),
    url(r'^dvds/(?P<slug>[-_\w]+)/add-senddvd/$', JobCreateSendDVDView.as_view(),
        name='job-create-senddvd'),
    url(r'^blurays/(?P<slug>[-_\w]+)/add-sendbluray/$', JobCreateSendBlurayView.as_view(),
        name='job-create-sendbluray'),
)