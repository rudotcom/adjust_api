from django.contrib import admin
from django.urls import path
from api.views import DataList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DataList.as_view(), name='data'),
]
