from django.shortcuts import render
from django.views import View
from users.forms import UserForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

class UserViewCreate(CreateView):
    model = User
    success_url = '/blog/'
    template_name = "home-user.html"
    form_class = UserForm


class UserViewUpdate(UpdateView):
    model = User
    success_url = '/blog/'
    form_class = UserForm
    template_name = "home-user.html"

    def get_object(self):
        return self.request.user


class UserViewDelete(View):
    template_name = "form-delete.html"

    def get(self, request, *args):
        return render(request,  self.template_name, {'user':request.user.username})

    def post(self, request, *args):
        User.objects.get(id=request.user.id).delete()
        return HttpResponseRedirect('/')