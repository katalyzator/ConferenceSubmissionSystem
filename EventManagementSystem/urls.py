from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from EventManagementSystem import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'conference.views.index_view', name='index'),
    url(r'^event/', 'conference.views.event_view', name='event'),
    url(r'^events/(?P<id>\d+)/$', 'conference.views.single_conference', name='single'),
    url(r'^get_application/(?P<id>\d+)/$', 'conference.views.get_application', name='get_application'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
