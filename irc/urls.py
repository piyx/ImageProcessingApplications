from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image-to-text', views.image_to_text, name='image-to-text'),
    path('image-classification', views.image_classification, name='image-classification'),
    path('image-restoration', views.image_restoration, name='image-restoration')
]







