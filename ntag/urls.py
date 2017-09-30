from django.conf.urls import url
from . import views
from django.conf import settings



urlpatters = [
	url(r'^$', views.TagAdd),
	url(r'^$', views.TagDisplay),
	url(r'^(?<tag_id>\d+)/$', views.TagDisplayCurrent)
]


urlpatterns += patterns('', url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)