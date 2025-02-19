from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from packages.filters import PackageFilters
from .models import Package
from .forms import PackageForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from acl.mixins import PermissionMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Package

def upload_media(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == "POST" and request.FILES:
        files = request.FILES.getlist("files")
        file_urls = []
        
        for file in files:
            file_path = f"media/packages/{file.name}"
            with open(file_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            file_urls.append(file_path)

        package.media_files += file_urls
        package.save()
        
        return JsonResponse({"message": "فایل‌ها با موفقیت ذخیره شدند!", "files": file_urls})

    return JsonResponse({"error": "درخواست نامعتبر است"}, status=400)


class PackageListView(ListView):
    model = Package
    template_name = 'packages/package_list.html'
    context_object_name = 'packages'


class PackageDetailView(DetailView):
    model = Package
    template_name = 'packages/package_detail.html'
    context_object_name = 'package'


#? ============================= Package CRUD =============================
class PackageListViewAdmin(PermissionMixin, ListView):
    permissions = ['Package_list']
    model = Package
    context_object_name = 'Package_list'
    template_name = 'packages/package_admin_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return PackageFilters(data=self.request.GET, queryset=queryset).qs


class PackageCreateViewAdmin(PermissionMixin, CreateView):
    permissions = ['Package_create']
    template_name = 'packages/package_admin_form.html'
    model = Package
    form_class = PackageForm
    success_url = reverse_lazy("package-admin-list")


class PackageUpdateViewAdmin(PermissionMixin, UpdateView):
    permissions = ['Package_list_edit']
    template_name = 'packages/package_admin_form.html'
    model = Package
    form_class = PackageForm
    success_url = reverse_lazy("package-admin-list")


class PackageDeleteViewAdmin(PermissionMixin, DeleteView):
    permissions = ['Package_list_delete']
    model = Package
    template_name = 'packages/confirm_package_delete.html'
    success_url = reverse_lazy("package-admin-list")
