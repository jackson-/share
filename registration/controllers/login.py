from registration.forms.user_form import UserForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate

class Login(View):

    template_name = 'store/templates/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                print "ACTIVE"
                login(request,user)
                return redirect('/')
            else:
                print "DISABLED"
                 # Return a 'disabled account' error message
                return render(request, self.template_name)
        else:
            print "INVALID"
             # Return a 'invalid login'  error message
            return redirect('/')
        print "LAST TRESORT"
        return render(request, self.template_name)