from django.db import models
from django.utils import timezone

class Bidhaa(models.Model):
    bidhaa_jina = models.CharField(max_length=264)
    bidhaa_shipping_cost = models.IntegerField()
    bidhaa_published = models.DateTimeField(default=timezone.now)
    bidhaa_country = models.CharField(max_length=264)
    bidhaa_shipping_days = models.IntegerField()
    # bidhaa_picha = models.FileField(upload_to=)

    def __str__(self) -> str:
        return self.bidhaa_jina

    def __str__(self) -> str:
        return self.bidhaa_country

    def __str__(self) -> str:
        return str(self.bidhaa_shipping_cost)


# class AccessRecord(models.Model):
    # jina = models.ForeignKey(Bidhaa)
    # tarehe = models.DateTimeField()

    # def __str__(self) -> str:
    #     return str(self.tarehe)



