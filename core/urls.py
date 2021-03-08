from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponsePermanentRedirect as redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'), namespace="blog")),
    path('user/', include(('users.urls', 'users'), namespace="users")),
    path('auth/', include('django.contrib.auth.urls')),
    path('', lambda _: redirect('blog'), name="home-redirect"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
