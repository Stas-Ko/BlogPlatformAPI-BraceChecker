from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from posts.views import home  



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('', home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




