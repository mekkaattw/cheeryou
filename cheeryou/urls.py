from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('Registration.views',
# Examples:
# url(r'^$', 'refproj.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
url(r'^admin/', include(admin.site.urls)),
url(r'^hello/$', 'Registration'),
)

