from django.urls import path
from .views import PackageListView, PackageDetailView, upload_media, PackageListViewAdmin, PackageCreateViewAdmin, PackageUpdateViewAdmin, PackageDeleteViewAdmin

app_name = 'packages'

urlpatterns = [
    path('', PackageListView.as_view(), name='package_list'),
    path('<int:pk>/', PackageDetailView.as_view(), name='package_detail'),

    path('list', PackageListViewAdmin.as_view(), name='package-admin-list'),
    path('create/', PackageCreateViewAdmin.as_view(), name='package-create'),
    path('update/<int:pk>/', PackageUpdateViewAdmin.as_view(), name='package-update'),
    path('delete/<int:pk>/', PackageDeleteViewAdmin.as_view(), name='package-delete'),
]
