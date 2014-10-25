from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from moneytalks.forms import MyLoginForm, MyPasswordChangeForm
from moneytalks.views import MyRegistration


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
                       url(r'^accounts/', include('accounts.urls')),
                       url(r'^places/', include('places.urls')),
                       url(r'^categories/', include('categories.urls')),
                       url(r'^login/$', auth_views.login,
                           {'template_name': 'registration/login.html',
                            'authentication_form': MyLoginForm},
                           name='auth_login'),
                       url(r'^logout/$', auth_views.logout,
                           {'next_page': '/'},
                           name='auth_logout'),
                       url(r'^register/$',
                           MyRegistration.as_view(),
                           name='registration_register'),
                       url(r'^register/complete/$',
                           TemplateView.as_view(template_name='index.html'),
                           name='registration_complete'),
                       url(r'^password/change/$',
                           auth_views.password_change,
                           {'post_change_redirect': reverse_lazy('auth_password_change_done'),
                           'password_change_form': MyPasswordChangeForm},
                           name='auth_password_change'),
)
