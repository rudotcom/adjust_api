from rest_framework import generics
from rest_framework.response import Response

from api.serializers import DataSetSerializer
from api.models import SampleDataSet
from django.db.models import Sum


class DataList(generics.ListAPIView):
    queryset = SampleDataSet.objects.all()

    def list(self, request, *args, **kwargs):
        query_params = self.request.query_params
        queryset = self.get_queryset()
        show = []

        for key in query_params.keys():

            if key == 'group_by':
                group_by = query_params['group_by'].split(',')
                queryset = queryset.values(*group_by)
            elif key == 'date_from':
                date_from = query_params['date_from']
                queryset = queryset.filter(date__gte=date_from)
            elif key == 'date_to':
                date_to = query_params['date_to']
                queryset = queryset.filter(date__lte=date_to)
            elif key == 'channel':
                channel = query_params['channel'].split(',')
                queryset = queryset.filter(channel__in=channel)
            elif key == 'country':
                country = query_params['country'].split(',')
                queryset = queryset.filter(country__in=country)
            elif key == 'os':
                os = query_params['os']
                queryset = queryset.filter(os=os)
            elif key == 'order_by':
                order_by = query_params['order_by'].split(',')
            elif key == 'show':
                show = query_params['show'].split(',')

        queryset = (queryset
                    .annotate(
                        cpi=Sum('spend')/Sum('installs'),
                        clicks=Sum('clicks'),
                        impressions=Sum('impressions'),
                        installs=Sum('installs'),
                        spend=Sum('spend'),
                        revenue=Sum('revenue'),
                    )

                    .order_by(*order_by)
                    )

        # fields to pass to serializer including those from order_by without minus sign
        fields = group_by + show
        for order in order_by:
            fields.append(order.replace('-', ''))

        serializer = DataSetSerializer(queryset, many=True, fields=fields)
        return Response(serializer.data)
