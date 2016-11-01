from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'app_main.views.home', name='home'),
    url(r'^login_propietario/', 'app_main.views.login_propietario', name='login_propietario'),
    url(r'^login_alumno/', 'app_main.views.login_alumno', name='login_alumno'),

    url(r'^publicar_casa/', 'app_main.views.publicar_casa', name='publicar_casa'),


    # url(r'^blog/', include('blog.urls')),
    url(r'^propietarios/', include('propietarios.urls')),
    url(r'^casas/', include('casas.urls')),



    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)
