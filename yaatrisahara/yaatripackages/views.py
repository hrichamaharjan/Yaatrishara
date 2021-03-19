from django.shortcuts import render

from .models import Package,Location
from django.views.generic import ListView,DetailView
def Home(request):
    context={'package':Package.objects.all()}

    return render(request,'yaatripackages/packages.html',context)
def packages(request):



    all_package = []
    packages = Package.objects.all().filter()
    for p in packages:

        location = Location.objects.all().filter(package__id=p.id)
        for l in location:
            print(l)
        all_package.append({p: location})
    print(all_package)
    context = {
        'packages': all_package,
        'title': 'Blog',
        }
    return render(request, 'yaatripackages/packages.html', context)

# class PackageListView(ListView):
#     model=Package
#     template_name='yaatripackages/packages.html'
#     context_object_name='packages'
#     paginate_by =2
class PackageDetailView(DetailView):
    model=Package

