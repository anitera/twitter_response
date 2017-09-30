from django.conf.urls import url
from . import views

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatters = [
	url(r'^$', views.TagAdd),
	url(r'^$', views.TagDisplay),
	url(r'^(?<tag_id>\d+)/$', views.TagDisplayCurrent)
]
