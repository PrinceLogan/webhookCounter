from django.db import models
from django.utils import timezone
#from django import hstore

class PackageString(models.Model):
    string_uuid = models.CharField(max_length=36)
    source = models.CharField(max_length=65)
    def __str__(self):
        return '%s - %s' % (self.id, self.source)

class WebhookTransaction(models.Model):
    body = models.TextField()
    date_received = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return u'{0}'.format(self.date_received)
