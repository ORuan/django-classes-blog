from django.urls import path, include
from users.views import UserViewCreate, UserViewUpdate, UserViewDelete
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

    path('create/', UserViewCreate.as_view(), name="user-view-home"),
    path('update/', login_required(UserViewUpdate.as_view(), login_url="/login/"), name="user-view-update"),
    path('delete/', login_required(UserViewDelete.as_view()), name="user-view-delete"),


]