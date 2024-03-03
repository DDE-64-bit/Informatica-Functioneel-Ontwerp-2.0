from django.db import models
from django.conf import settings

class Hond(models.Model):
    naamHond = models.CharField(max_length=100)
    eigenaarNaam = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plaats = models.CharField(max_length=100)
    zichtbaar_op_site = models.BooleanField(default=False)

    def __str__(self):
        return self.naamHond