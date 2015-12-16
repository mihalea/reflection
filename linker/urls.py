from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/', views.add, name="add"),
    url(r'^action/add/', views.add_action, name="add_action"),
    url(r'^$', views.index, name="index"),
]
