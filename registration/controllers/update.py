from registration.forms.user_form import UserForm
from django.shortcuts import render, redirect
from django.views.generic import View

class Update(View):

    template_name = 'registration.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass