from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('login/', AuthenticationUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('hotels/<slug:slug>/', test, name='hotel_detailed'),
    path('logout/', logout_user, name='logout'),
    path('tours/<slug:slug>/', test_tour, name='detailed_tour'),
    path('hotels/', AllHotelsList.as_view(), name='hotels')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)