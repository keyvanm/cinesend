from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('asset_portal.views',
    url(r'^assets/$', AssetListView.as_view(), name='asset-list'),
    url(r'^assets/add/$', AssetCreateView.as_view(), name='asset-create'),
    url(r'^assets/(?P<slug>[-_\w]+)/$', AssetDetailView.as_view(), name='asset-detail'),
    url(r'^assets/(?P<slug>[-_\w]+)/tracking/$', AssetTrackingView.as_view(), name='asset-tracking'),
    url(r'^assets/(?P<slug>[-_\w]+)/edit/$', AssetEditView.as_view(), name='asset-edit'),
    url(r'^assets/(?P<slug>[-_\w]+)/delete/$', AssetDeleteView.as_view(), name='asset-delete'),


    url(r'^jobs/$', JobListView.as_view(), name='job-list'),

    # url(r'^assets/(?P<slug>[-_\w]+)/add-logochange/$', JobCreateLogoChangeView.as_view(),
    #     name='job-create-logochange'),
    # url(r'^assets/(?P<slug>[-_\w]+)/add-qualitycheck/$', JobCreateQualityCheckView.as_view(),
    #     name='job-create-qualitycheck'),
    # url(r'^assets/(?P<slug>[-_\w]+)/add-physicaldcp/$', JobCreatePhysicalDCPView.as_view(),
    #     name='job-create-physicaldcp'),
    url(r'^assets/(?P<slug>[-_\w]+)/add-encodedcp/$', JobCreateMakeDCPView.as_view(),
        name='job-create-makedcp'),
    url(r'^assets/(?P<slug>[-_\w]+)/add-encodedvd/$', JobCreateEncodeDVDView.as_view(),
        name='job-create-encodedvd'),
    url(r'^assets/(?P<slug>[-_\w]+)/add-encodebluray/$', JobCreateEncodeBlurayView.as_view(),
        name='job-create-encodebluray'),

    url(r'^jobs/(?P<slug>[-_\w]+)/$', JobDetailView.as_view(), name='job-detail'),
    url(r'^jobs/(?P<slug>[-_\w]+)/edit/$', JobEditView.as_view(), name='job-edit'),
    url(r'^jobs/(?P<slug>[-_\w]+)/delete/$', JobDeleteView.as_view(), name='job-delete'),

    url(r'^flights/$', FlightListView.as_view(), name='flight-list'),
    url(r'^flights/(?P<pk>\d+)/$', FlightDetailView.as_view(), name='flight-detail'),


    url(r'^accounting/$', JobPayListView.as_view(), name='accounting-home'),
    url(r'^accounting/cart/$', JobCartView.as_view(), name='accounting-cart'),
)

