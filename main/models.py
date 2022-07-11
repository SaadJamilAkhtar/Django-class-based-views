from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.name
