
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from sweets import views







urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', include('sweets.urls')),

]

