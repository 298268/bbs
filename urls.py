from django.conf.urls import url
from . import views


urlpatterns=[url(r'^$',views.show),
             url(r'^forum/(\d+)/$',views.forumid,name="forum"),
             url(r'^article/(\d+)/$', views.articleid, name="article"),
             url(r'^article/post/$', views.articlepost, name="post"),
             url(r'^reply/(\d+)$', views.articlereply, name="reply"),
             url(r'^register/$', views.userregister, name="register"),
             url(r'^logout/$', views.userlogout, name="logout"),
             url(r'^login/$', views.userlogin, name="login"),]
