from django.urls import path
from .views import DataList

app_name = 'api'

urlpatterns = [
    # Single endpoint
    path('', DataList.as_view(), 'data'),
]
