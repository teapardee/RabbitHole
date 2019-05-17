from django.urls import path, re_path
from . import views


urlpatterns = [

    path("", views.one),
    path('<str:cat_id>/', views.two),
    path('<str:cat_id>/<str:subcat_id>/', views.three),
    path('<str:cat_id>/<str:subcat_id>/<str:channel_id>/', views.four),
]