from django.db import models


class TestElementA(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TestElementB(models.Model):
    name = models.CharField(max_length=50)
    ace = models.ManyToManyField(TestElementA)

    def __str__(self):
        return self.name


class TestElementC(models.Model):
    name = models.CharField(max_length=50)
    bees = models.ManyToManyField(TestElementB)

    def __str__(self):
        return self.name
