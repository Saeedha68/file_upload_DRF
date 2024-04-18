from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_view


app_name = 'fileupload'
urlpatterns = [
    path('',views.main,name='main'),
    path('imageupload/', views.ImageUpload.as_view(), name='ImageUpload'),
    path('documentupload/', views.DocumentUpload.as_view(), name='DocumentUpload'),
    path('metadata/', views.DocMetadata.as_view(), name='Metadata'),
    path('DeleteDocument/', views.DeleteDocument.as_view(), name='DeleteDocument'),
    path('DeleteImage/', views.DeleteImage.as_view(), name='DeleteImage'),
    path('factory/', views.Factory.as_view(), name='factory'),
    path('api-token-auth/', auth_view.obtain_auth_token),
]

