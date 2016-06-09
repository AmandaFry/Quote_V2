from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	
	url(r'^favorite/$', views.favorite, name='favorite'),
	url(r'^clear/$', views.clear, name='clear'),
	url(r'^updateMe/$', views.edit, name='edit'),
	url(r'^addEdit/$', views.addEdit, name='addEdit'),
	url(r'^new/$', views.new, name='new'),
	url(r'^addNew/$', views.addNew, name='addNew'),
	url(r'^successAE/$', views.successAE, name='successAE'),
	url(r'^$', views.index, name='index'),
]

