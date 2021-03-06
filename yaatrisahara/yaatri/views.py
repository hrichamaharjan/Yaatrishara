from django.shortcuts import render
from .models import Post



def home(request):



    return render(request,'yaatri/index.html')
def blog(request):
    context={
        'posts': Post.objects.all(),
        'title':'Blog'
    }

    return render(request,'yaatri/blog.html',context)

# Create your views here.
