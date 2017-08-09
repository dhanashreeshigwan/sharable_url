"""question1 URL Configuration

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
import views
from django.conf.urls import url, include
from django.contrib import admin
from .apps.snippet import urls as snippet_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.SnippetView.as_view(),name='snip_data'),
    url(r'^snippet/(?P<snippet_id>\w+)/$',views.KeyLogin.as_view(),\
        name='keylogin'),
    url(r'^snippet/$', views.SnippetDetailView.as_view(), \
        name='snippetDetail'),
    url(r'^admin/', admin.site.urls),
    url(r'^snipapp/', include(snippet_urls, namespace='snippet')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
]
