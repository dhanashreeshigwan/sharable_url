# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Snippet(models.Model):
    data = models.CharField(max_length=100,null=False)
    key = models.CharField(max_length=50,null=True,unique=True)
    url = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.data