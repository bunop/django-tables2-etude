from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')
    info = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.info)
