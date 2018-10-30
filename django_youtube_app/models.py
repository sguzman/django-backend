# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ChanStats(models.Model):
    time = models.DateTimeField()
    serial = models.CharField(max_length=24)
    subs = models.BigIntegerField()
    videos = models.IntegerField()
    views = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'chan_stats'