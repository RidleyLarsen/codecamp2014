from django.conf.urls import patterns, include, url
from django.contrib import admin

from app.views import Homepage

urlpatterns = patterns(
    '',
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', Homepage.as_view(), name="homepage"),
)
