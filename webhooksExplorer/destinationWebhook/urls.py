#from django.urls import path
from destinationWebhook import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reciever$', views.reciever, name='reciever'),
    ]
