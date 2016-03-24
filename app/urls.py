from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('status', views.status, name='status'),
    url('switch/(?P<b>.+)', views.switch, name='switch'),
]
