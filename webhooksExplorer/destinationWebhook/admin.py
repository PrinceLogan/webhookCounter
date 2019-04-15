from django.contrib import admin
from .models import PackageString
from .models import WebhookTransaction

admin.site.register(PackageString)
admin.site.register(WebhookTransaction)
