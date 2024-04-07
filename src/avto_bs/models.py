from django.db import models

class z_avtobrand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    class Meta:
        db_table = 'z_avtobrand'

class z_avtomodel(models.Model):
    BrandID = models.ForeignKey(z_avtobrand, on_delete=models.CASCADE)
    ModelID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    class Meta:
        db_table = 'z_avtomodel'

class z_avtocolor(models.Model):
    ColorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    class Meta:
        db_table = 'z_avtocolor'