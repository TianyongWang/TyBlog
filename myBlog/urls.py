"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from article import views
# from DjangoUeditor import urls as djud_urls
# from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home),
    # url(r'^(?P<my_args>\d+)/$',views.detail),
    # url(r'^ueditor/',include('DjangoUeditor.urls' )),
    # url(r'^ueditor/',DjangoUeditor.urls),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name = 'archives'),
    url(r'^aboutme/$', views.about_me, name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
]
# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
