from django.urls import path
from blog.views import BlogView, AbotView

urlpatterns = [
    path('', BlogView.as_view(), name="blog-view-home"),
    path('about/', AbotView.as_view(), name="about-view-home")
]