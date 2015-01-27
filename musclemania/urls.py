from django.conf.urls import patterns, include, url
from django.contrib import admin
from categories.views import categories_menu

urlpatterns = patterns('',
    url(r'^$', 'categories.views.categories_menu', name='categories menu'),
    url(r'^admin/', include(admin.site.urls)),
)
