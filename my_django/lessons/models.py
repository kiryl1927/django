from django.db import models

class Model1(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return str(self.pole1) + ' ' + str(self.pole2)

class Model2(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=200)
    pole3 = models.TextField()

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return str(self.pole1) + ' ' + str(self.pole2)
class Model3(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return str(self.pole1) + ' ' + str(self.pole2)