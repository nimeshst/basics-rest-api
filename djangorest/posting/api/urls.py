from .views import BlogPostRudView
from .views import BlogPostAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', BlogPostAPIView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
]
