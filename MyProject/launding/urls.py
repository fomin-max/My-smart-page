from django.conf.urls import url

from launding import views

urlpatterns = [
    url(r'^mysite/$', views.launding, name='launding'),
    # url(r'^myfeed/$', feeds.pull_feed),
]
