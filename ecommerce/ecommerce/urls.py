from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/', include('chat.api.urls', namespace='api')),
    path('account/', include('accounts.urls', namespace='account')),
    path('', include('products.urls', namespace='mainapp')),
    path('', include('checkout.urls', namespace='checkout')),
    path('chat/', include('chat.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
