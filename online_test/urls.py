from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('class/',views.classes),
    path('class/<int:number>/',views.items),
    path('class/<int:number>/<str:pk>',views.item_detail)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
