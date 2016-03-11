from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from fineDonor import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'services.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/',views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),)
)
