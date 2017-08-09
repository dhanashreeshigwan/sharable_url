from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from shreableUrl.apps.snippet import views

router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^snippet_list/$', views.SnippetList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)