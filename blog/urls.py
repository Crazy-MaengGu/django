from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
path('blog/hi1', views.post_list2, name='post_list'),
path('blog/hi2', views.post_list3, name='post_list'),
]


# http://www.~~~~.com/blog/