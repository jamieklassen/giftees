from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import app.urls


admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^$',
        login_required(TemplateView.as_view(template_name="index.html")),
        name='home'),
    url(r'^api/', include(app.urls)),

    url(r'^login/?$',
        'django.contrib.auth.views.login',
        {
            'template_name':
            '/Library/Python/2.7/site-packages/django/contrib' +
            '/admin/templates/admin/login.html',
        }),

    url(r'^logout/?$', 'django.contrib.auth.views.logout'),

    url(r'^admin/doc/',
        include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
