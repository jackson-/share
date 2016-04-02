
from django.conf.urls import url, include
from django.contrib import admin
from store.controllers.items_view import ItemsView
from store.controllers.stores_view import StoresView
urlpatterns = [
    url(r'^store/(?P<store_id>[0-9]+)/', ItemsView.as_view()),
    url(r'^', StoresView.as_view()),
]
