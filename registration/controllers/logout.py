from registration.forms.user_form import UserForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout

class Logout(View):

    template_name = 'registration.html'

    def get(self, request):
        print 'GET'
        logout(request)
        return redirect('/')

    def post(self, request):
        print "POST"
        logout(request)
        return redirect('/')