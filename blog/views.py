from django.shortcuts import render
from django.views import View
from blog.models import Post

data = [
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "Today the post is vagabond",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "Jane Done",
        "title": "Blog Post 2",
        "content": "Today the post is second vagadond",
        "date_posted": "August 28, 2020",
    }
]


class BlogView(View):
	def get(self, request):
		context = {
			'posts': Post.objects.all()
		}
		return render(request, 'blog/home.html', context)


class AbotView(View):
	def get(self, request):
		return render(request, 'blog/about.html')