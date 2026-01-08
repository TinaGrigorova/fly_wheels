from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import home
from store.views import index
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProductSitemap, CategorySitemap, StaticSitemap
from django.views.static import serve
from django.urls import re_path

handler404 = "store.views.custom_404"

sitemaps = {
    "products": ProductSitemap,
    "static": StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('shop/', include('products.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain"
    ), name="robots"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
