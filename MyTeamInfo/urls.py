from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MyTeamInfo API",
        default_version='v1',
        description="Test MyTeamInfo API",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainApp.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
