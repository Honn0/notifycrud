from django.db import models


class cadastro(models.Model):
    database = models.CharField(max_length=100)
    table = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    definir = models.CharField(max_length=100)
    definir = models.CharField(max_length=100)
    definir = models.CharField(max_length=100)
    script_conf = models.CharField(max_length=200)


