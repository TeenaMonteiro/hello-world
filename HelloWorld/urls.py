from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

     url(r'^login', 'HelloWorld.views.login', name='login'),
     
    url(r'^users/$', 'HelloWorld.views.list_users', name='list_users'),
     
    url(r'^admin/', include(admin.site.urls)),
)



