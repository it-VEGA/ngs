from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('news/',include('news.urls')),
    path('online_test/',include('online_test.urls')),
    path('contact',include('contact.urls'))
]
