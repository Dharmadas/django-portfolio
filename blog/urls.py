from django.urls import path
from . import views

urlpatterns = [
    path('', views.allBlogs, name="all-blogs"),
    path('<int:blog_id>/', views.detail, name="detail")
]
