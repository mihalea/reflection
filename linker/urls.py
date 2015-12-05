from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)', views.show, name="show"),
    url(r'^', views.index, name="index"),
]
