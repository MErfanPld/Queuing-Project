from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Package
from .forms import PackageForm


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
