from django.conf.urls import url
from . import views
	
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^group/(?P<pk>[0-9]+)/details/$', views.userGroup_detail, name='userGroup_detail'),
	url(r'^group/new/$', views.userGroup_new, name='userGroup_new'),
	url(r'^group/(?P<pk>[0-9]+)/edit/$', views.userGroup_edit, name='userGroup_edit'),
	url(r'^group/(?P<pk1>[0-9]+)/shoplist/(?P<pk2>[0-9]+)$', views.shopList_detail, name='shopList_detail'),
	url(r'^group/(?P<pk>[0-9]+)/shoplist/new/$', views.shopList_new, name='shopList_new'),
	
]