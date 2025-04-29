from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


from authentication.views.authentication import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', ShowProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

