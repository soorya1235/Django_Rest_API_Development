"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from Blogger.api import PostList , PostList1 ,PostDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/post_list/$',PostList.as_view(),name='post_list'),
    url(r'^api1/post_list_postmethod/$', PostList1.as_view(), name='post_list'),
    url(r'^api/post_list_one/(?P<post_id>\d+)$', PostDetails.as_view(), name='post_list')
]
