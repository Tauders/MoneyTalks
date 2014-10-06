from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'moneytalks.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^transactions/', include('transactions.urls')),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       url(r'^accounts/profile/', TemplateView.as_view(template_name='registration/profile.html'),
                           name='auth_profile'),
                       url(r'^places/', include('places.urls')),
                       url(r'^categories/', include('categories.urls')),
)
