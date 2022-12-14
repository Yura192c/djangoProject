from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    #path('cart/', include('cart.urls')),
    path('shop/', include('shop.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    #path('shop/', include(('shop.urls', 'shop'), namespace='shop'))
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
