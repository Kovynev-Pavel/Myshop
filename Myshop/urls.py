from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # url адрес страницы админ панели, переход на неё. В '' начало url адреса страницы
    path('', include('main.urls')),  # Перенос рабыты с url адресами приложению main
    path('products/', include('products.urls')),  # Перенос рабыты с url адресами приложению products
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Для работы статичных файлов

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Для работы с изображениями
