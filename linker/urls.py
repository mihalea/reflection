from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^show/(?P<id>[0-9]+)', views.show, name="edit"),
    url(r'^', views.index, name="index"),
]
