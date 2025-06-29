from django.db import models

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    state_id = models.IntegerField()

class AnnouncedPuResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()

class Lga(models.Model):
    lga_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()