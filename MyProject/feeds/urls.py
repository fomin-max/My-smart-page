from django.conf.urls import url

from feeds.templatetags import feeds
from launding import views

urlpatterns = [
    url(r'^mysite/$', views.launding, name='launding'),
    url(r'^myfeed/$', feeds.pull_feed, name='pull_feed'),

]
