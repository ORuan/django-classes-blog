from django.shortcuts import render
from django.views import View
from blog.models import Post
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from blog.forms import PostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse

class BlogViewList(ListView):
    model = Post
    template_name = "blog/home.html"


class BlogViewCreate(CreateView):
    model = Post
    success_url = '/blog/'
    template_name = "form/form-post.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class BlogViewUpdate(UpdateView):
    model = Post
    success_url = '/blog/'
    template_name = "form/form-post.html"
    form_class = PostForm


class AbotView(View):
    def get(self, request):
        return render(request, 'blog/about.html')

class BlogViewDelete(View):
    template_name = "form/form-delete-post.html"
    #, {'post':Post.objects.get(id=0)}
    def get(self, request, id, *args):
        post = Post.objects.get(id=id)
        if request.user.id == post.author.id: 
            return render(request,  self.template_name)
        else:
            return HttpResponseNotFound('ERROR')
    def post(self, request, id, *args):
        post = Post.objects.get(id=id)
        if request.user.id == post.author.id: 
            post.delete()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('<h1 class="text-center">Coe meno, não pode fazer isso</h1>')