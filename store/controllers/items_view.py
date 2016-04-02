from django.shortcuts import render, redirect
from django.views.generic import View
from store.models import Store, Item

class ItemsView(View):

    template_name = "index.html"

    def get(self, request, **kwargs):
        print "LIST"
        store = Store.objects.get(id=kwargs['store_id'])
        items = Item.objects.get(store)
        return render(request, self.template_name, {'items':items})

    def post(self, request):
        pass