from django.urls import include,path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'

urlpatterns = [
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
    url(r'^accounts/register/$',
        MyRegistrationView.as_view(),
           name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
