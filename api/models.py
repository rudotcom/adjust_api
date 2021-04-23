from django.db import models


class SampleDataSet(models.Model):

    CHANNELS = (
        ('chartboost', 'chartboost'),
        ('apple_search_ads', 'apple_search_ads'),
        ('adcolony', 'adcolony'),
        ('google', 'google'),
        ('unityads', 'unityads'),
        ('vungle', 'vungle'),
        ('facebook', 'facebook'),
    )
    OS = (
        ('os', 'OS'),
        ('android', 'Android'),
    )

    date = models.DateField(verbose_name='Date')
    channel = models.CharField(max_length=25, choices=CHANNELS, verbose_name='Advertising channel')
    country = models.CharField(max_length=2, verbose_name='ISO 3166-1 alpha-2')
    os = models.CharField(max_length=10, choices=OS, verbose_name='Operating System')
    impressions = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    installs = models.PositiveIntegerField()
    spend = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Expenses')
    revenue = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Revenue')
