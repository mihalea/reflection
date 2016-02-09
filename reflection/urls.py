from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^git/', include('linker.urls', namespace='linker')),
    url(r'^', include('presenter.urls', namespace='presenter')),
]

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
