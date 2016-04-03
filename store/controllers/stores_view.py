from django.shortcuts import render, redirect
from django.views.generic import View
from store.models import Store
from registration.models.user import MyUser
from django.contrib.auth import authenticate



class StoresView(View):

    template_name = "index.html"

    def get(self, request):
        # user = authenticate(username='new@mail.com', password='123')
        stores = Store.objects.all()
        return render(request, self.template_name, {'stores':stores})

    def post(self, request):
        pass