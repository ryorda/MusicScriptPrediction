from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^result/?', views.result, name='result'),
	url(r'^api/recomputeall/?', views.recomputeall, name='recomputeall'),
	url(r'^api/entry/song/?', views.entrysong, name='entrysong'),
	url(r'^debug/?', views.debug, name='debug')
]