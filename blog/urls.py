from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
]