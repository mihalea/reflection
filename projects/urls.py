from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^projects/$', views.showcase, name="showcase"),
    url(r'^projects/add$', views.add, name="add"),
    url(r'^projects/(?P<slug>[\w-]+)$', views.details, name="view"),
    url(r'^projects/(?P<slug>[\w-]+)/edit$', views.edit, name="edit"),
]
