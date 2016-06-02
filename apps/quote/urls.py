from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	
	# url(r'^showOne/$', views.showOne),
	url(r'^clear/$', views.clear, name='clear'),
	# url(r'^updateMe/$', views.updateMe, name='updateMe'),
	url(r'^new/$', views.new, name='new'),
	url(r'^addNew/$', views.addNew, name='addNew'),
	url(r'^$', views.index, name='index'),
]

