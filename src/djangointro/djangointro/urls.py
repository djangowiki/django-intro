from django.contrib import admin
from django.urls import path, include
from pages import urls
from products import urls as productUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('products/', include(productUrls))
]
