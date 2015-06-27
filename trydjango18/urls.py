from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^crime/$', 'newsletter.views.crime', name='crime'),
    url(r'^crime/aktau$', 'newsletter.views.aktau', name='aktau'),
    url(r'^crime/aktobe$', 'newsletter.views.aktobe', name='aktobe'),
    url(r'^crime/astana$', 'newsletter.views.astana', name='astana'),
    url(r'^crime/atyrau$', 'newsletter.views.atyrau', name='atyrau'),
    url(r'^crime/karaganda$', 'newsletter.views.karaganda', name='karaganda'),
    url(r'^crime/kokshetau$', 'newsletter.views.kokshetau', name='kokshetau'),
    url(r'^crime/kostanay$', 'newsletter.views.kostanay', name='kostanay'),
    url(r'^crime/kyzylorda$', 'newsletter.views.kyzylorda', name='kyzylorda'),
    url(r'^crime/pavlodar$', 'newsletter.views.pavlodar', name='pavlodar'),
    url(r'^crime/petropavlovsk$', 'newsletter.views.petropavlovsk', name='petropavlovsk'),
    url(r'^crime/shymkent$', 'newsletter.views.shymkent', name='shymkent'),
    url(r'^crime/taldykorgan$', 'newsletter.views.taldykorgan', name='taldykorgan'),
    url(r'^crime/taraz$', 'newsletter.views.taraz', name='taraz'),
    url(r'^crime/uralsk$', 'newsletter.views.uralsk', name='uralsk'),
    url(r'^crime/uskaman$', 'newsletter.views.uskaman', name='uskaman'),
    url(r'^dtp/$', 'newsletter.views.dtp', name='dtp'),
    url(r'^olimpkz/$', 'newsletter.views.olimpkz', name='olimpkz'),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

