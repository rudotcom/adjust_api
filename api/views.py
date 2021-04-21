from django.views.generic import ListView

from api.models import SampleDataSet


class DataList(ListView):
    model = SampleDataSet
    pass
