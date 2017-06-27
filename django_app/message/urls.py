from django.conf.urls import url

from . import views

app_name = 'message'
urlpatterns = [
    url(r'^send/$', views.sms_send, name='send'),
    url(r'^list/$', views.sms_list, name='list')
]
