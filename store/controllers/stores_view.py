from django.shortcuts import render, redirect
from django.views.generic import View
from store.models import Store


class StoresView(View):

    template_name = "index.html"

    def get(self, request):
        stores = Store.objects.all()
        return render(request, self.template_name, )

    def post(self, request):
        pass