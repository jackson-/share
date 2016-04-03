from registration.forms.user_form import UserForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate

class Registration(View):

    template_name = 'registration.html'

    def get(self, request):
        return render(request, self.template_name, {'form':UserForm()})

    def post(self, request):
        print "POST", request.POST
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.user = authenticate(username=user.email, password=user.password)
            return redirect('/')
        else:
            return render(request, self.template_name, {'form':form})