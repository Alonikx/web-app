from django.db import models


class BronTable(models.Model):
    name = models.CharField(max_length=90, blank=True, null=True)
    place_num = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    time_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bron-table'


class Places(models.Model):
    place_num = models.IntegerField(primary_key=True)
    place_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'