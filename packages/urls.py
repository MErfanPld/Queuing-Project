from django.urls import path
from .views import PackageListView, PackageDetailView, upload_media

app_name = 'packages' 

urlpatterns = [
    path('', PackageListView.as_view(), name='package_list'),
    path('<int:pk>/', PackageDetailView.as_view(), name='package_detail'),
    path('<int:package_id>/upload-media/', upload_media, name='upload_media')

]
