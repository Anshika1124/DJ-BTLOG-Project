from django.urls import path
from .views import about_blog,detail_blog

urlpatterns = [
	path('',about_blog,name="about"),
	path('blog/<int:id>/',detail_blog,name="detail"),
]

