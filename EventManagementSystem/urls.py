from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'conference.views.index_view', name='index'),
    url(r'^event/', 'conference.views.event_view', name='event'),
]
