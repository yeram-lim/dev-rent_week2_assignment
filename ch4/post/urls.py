from django.contrib import admin
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path("", views.base, name="base"),
    path('<int:pk>/', view = views.post_detail, name='detail'),
    path("write/", views.post_write, name="write"),
    path('<int:pk>/update/', view = views.post_update, name='update'),
    path('<int:pk>/delete/', view = views.post_delete, name='delete'),
    # path("/base/", views.base, name="base2"),
]
