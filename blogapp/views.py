from django.shortcuts import get_object_or_404 , render
from .models import Blog

# Create your views here.
def about_blog(request):  
   obj = Blog.objects.all()
   return render(request, "about.html", {"about": obj})  

def detail_blog(request,id):
    obj=get_object_or_404(Blog,id=id)
    return render(request,"detail.html",{"detail":obj})

