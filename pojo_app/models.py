from django.db import models

# Create your models here.

class Pojo_Data(models.Model):
    Month= models.CharField(max_length=20)
    Company=models.CharField(max_length=50)
    No_of_stocks_above_200_EMA=models.IntegerField(default=0)
    percentage_of_stocks_above_200_EMA=models.FloatField(default=0)
    No_of_stocks_above_100_EMA=models.IntegerField(default=0)
    percentage_of_stocks_above_100_EMA=models.FloatField(default=0)
    No_of_stocks_above_50_EMA=models.IntegerField(default=0)
    percentage_of_stocks_above_50_EMA=models.FloatField(default=0)

