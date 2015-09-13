from allauth.account.signals import password_set, password_reset, password_changed
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import update_session_auth_hash
from django.views.generic.base import TemplateView
from django_markdown import flatpages

import views
import user_manager


flatpages.register()

urlpatterns = patterns('',
                       url(r'^accounts/address/', include('user_manager.addr_urls')),
                       url(r'^pages/', include('django.contrib.flatpages.urls')),
                       url(r'^about/', TemplateView.as_view(template_name='static-content/about.html')),
                       url(r'^accounts/', include('allauth.urls')),
                       url(r'^markdown/', include('django_markdown.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^select2/', include('django_select2.urls')),
                       url(r'^portal/', include('asset_portal.urls')),
                       url(r'^vault/', include('vault.urls')),
                       url(r'^$', views.homepage, name='homepage'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = TemplateView.as_view(template_name="500.html")


# To prevent logging users out upon password change
def update_session_hash_signal_receiver(sender, **kwargs):
    user = kwargs["user"]
    request = kwargs["request"]
    update_session_auth_hash(request, user)


password_changed.connect(update_session_hash_signal_receiver)
password_set.connect(update_session_hash_signal_receiver)
password_reset.connect(update_session_hash_signal_receiver)

