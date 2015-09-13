from django.contrib import admin

from vault.models.dcp import DCP
from vault.models.optical_disc import DVD, Bluray

admin.site.register(DCP)
admin.site.register(DVD)
admin.site.register(Bluray)
