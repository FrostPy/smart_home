from django.db import models
from django.db.models import CASCADE


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название датчика')
    description = models.CharField(max_length=50, verbose_name='Описание датчика')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=CASCADE, related_query_name='measurement')
    temperature = models.DecimalField(max_digits=10, verbose_name='Измирение датчика')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')
