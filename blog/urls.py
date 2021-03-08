from django.urls import path
from blog.views import BlogViewCreate, AbotView, BlogViewList, BlogViewUpdate, BlogViewDelete
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('', BlogViewList.as_view(), name="blog-view-home"),
    path('create/', login_required(BlogViewCreate.as_view()), name="blog-view-create"),
    path('update/<int:pk>/', login_required(BlogViewUpdate.as_view()), name="blog-view-update"),
    path('delete/<int:id>/', login_required(BlogViewDelete.as_view()), name="blog-view-delete"),
    path('about/', AbotView.as_view(), name="about-view-home")
]