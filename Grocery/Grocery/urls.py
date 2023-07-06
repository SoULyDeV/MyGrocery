from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from products import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('users', include('users.urls')),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('cart/', include('cart.urls', namespace='cart')), 
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
