from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('wrapper.urls')),
    url(r'^.*$', RedirectView.as_view(url='admin/', permanent=False), name='main_index'),
]
