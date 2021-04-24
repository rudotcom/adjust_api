import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import DataSetSerializer
from api.models import SampleDataSet
from django.db.models import Sum


def validate_date(date_field):
    try:
        datetime.datetime.strptime(date_field, '%Y-%m-%d')
    except ValueError:
        context = {
            'exception': f'[{date_field}] value has an invalid date format.',
            'hint': f'Hint: Please ensure that filed format is \"YYYY-MM-DD\"',
        }
        return context


def check_fields(statement, fields):
    model_fields = [f.name for f in SampleDataSet._meta.get_fields()]

    for request_field in fields:
        if request_field not in model_fields:
            context = {
                'exception': f'Non-existent field name \"{request_field}\" in statement \"{statement}\".',
                'hint': f'Hint: Please check the field names in your statement \"{statement}\"',
            }
            return context


class DataList(generics.ListAPIView):
    queryset = SampleDataSet.objects.all()

    def list(self, request, *args, **kwargs):
        query_params = self.request.query_params
        queryset = self.get_queryset()
        show = []

        for key in query_params.keys():

            if key == 'group_by':

                group_by = query_params['group_by'].split(',')
                exception_context = check_fields('group_by', group_by)
                if exception_context:
                    return render(None, 'exception.html', exception_context)
                queryset = queryset.values(*group_by)

            elif key == 'date_from':
                date_from = query_params['date_from']
                exception_context = validate_date(date_from)
                if exception_context:
                    return render(None, 'exception.html', exception_context)
                queryset = queryset.filter(date__gte=date_from)

            elif key == 'date_to':
                date_to = query_params['date_to']
                exception_context = validate_date(date_to)
                if exception_context:
                    return render(None, 'exception.html', exception_context)
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
                exception_context = check_fields('order_by', order_by)
                if exception_context:
                    return render(None, 'exception.html', exception_context)

            elif key == 'show':
                show = query_params['show'].split(',')

        try:
            queryset = (queryset.annotate(
                                clicks=Sum('clicks'),
                                impressions=Sum('impressions'),
                                revenue=Sum('revenue'),
                                cpi=Sum('spend') / Sum('installs'),
                                installs=Sum('installs'),
                                spend=Sum('spend'),
                            )
                        )
        except ValueError:
            context = {
                'exception': 'Grouping parameters are inappropriate',
                'hint': 'Hint: Please check the parameters you use for grouping. '
                        'Appropriate ones are date, channel, country, os',
            }
            return render(None, 'exception.html', context)

        queryset = queryset.order_by(*order_by)
        # fields to pass to serializer including those from order_by without minus sign
        fields = group_by + show
        for order in order_by:
            fields.append(order.replace('-', ''))

        serializer = DataSetSerializer(queryset, many=True, fields=fields)
        return Response(serializer.data)
