from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^(?P<slug>[\w-]+)$', views.view, name="view"),
    url(r'^(?P<slug>[\w-]+)/edit$', views.edit, name="edit"),
]
