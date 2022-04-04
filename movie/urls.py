from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('getmovies', views.movies, name='movie'),
    path('top250', views.top_250, name='top250'),
    path('updateimage', views.update_image, name='updateimage'),
    path('upload', views.image_upload, name='upload'),
    path('view', views.view_image, name='view'),
    path('<slug:slug>/', views.comment_details, name='comment_details'),
    path('like/<int:m_id>/', views.likes, name='likes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
