"""
URL configuration for movie_gen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

app_name = "user_library"

from django.urls import path
from . import views 

urlpatterns = [
    # path('liked/<int:pk>', views.add_to_liked_movie, name='like_movie'),
    path('liked/<int:pk>/liked_content', views.user_liked_content_view, name='liked_view'),
    path('<int:pk>/watch_list', views.watch_list, name='watch_list'),
    path('Like/<str:content_type>/<int:object_id>', views.toggle_like, name='toogle_like')

]
