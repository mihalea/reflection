from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^update', views.update, name="update"),
    url(r'^add', views.add, name="add"),
    url(r'^id/(?P<id>[0-9]+)', views.view, name="view"),
]
