from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index_page, name="index"),
    path('image/', views.image_view, name='image-view'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
