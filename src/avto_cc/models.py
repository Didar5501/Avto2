from django.db import models
import uuid  

class country(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'country'

from django.contrib.auth.models import AbstractUser, Group, Permission

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'


from django.db import models
from avto_bs.models import z_avtobrand

class mcfcarbrand(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=100)
    idbs = models.IntegerField()
    country = models.ForeignKey("country", on_delete=models.CASCADE)
    creationdate = models.DateField()
    creationauthor = models.ForeignKey(User, related_name='created_mcfcarbrands', on_delete=models.CASCADE)
    changedate = models.DateField()
    changeauthor = models.ForeignKey(User, related_name='changed_mcfcarbrands', on_delete=models.CASCADE)
    mcfcode = models.CharField(max_length=100, default=id)

    class Meta:
        db_table = 'mcfcarbrand'

    def get_z_avtobrand(self):
        return z_avtobrand.objects.get(BrandID=self.idbs)

from avto_bs.models import z_avtomodel

class mcfcarmodel(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField()
    Name = models.CharField(max_length=100)
    carbrand = models.ForeignKey(mcfcarbrand, on_delete=models.CASCADE)
    idbs = models.IntegerField()
    creationdate = models.DateField()
    creationauthor = models.ForeignKey(User, related_name='created_mcfcarmodels', on_delete=models.CASCADE)
    changedate = models.DateField()
    changeauthor = models.ForeignKey(User, related_name='changed_mcfcarmodels', on_delete=models.CASCADE)
    mcfcode = models.CharField(max_length=100, default='id')

    class Meta:
        db_table = 'mcfcarmodel'

    def get_z_avtomodel(self):
        return z_avtomodel.objects.get(ModelID=self.idbs)

from avto_bs.models import z_avtocolor

class mcfcarcolor(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField()
    Name = models.CharField(max_length=100)
    idbs = models.IntegerField()
    creationdate = models.DateField()
    creationauthor = models.ForeignKey(User, related_name='created_mcfcarcolors', on_delete=models.CASCADE)
    changedate = models.DateField()
    changeauthor = models.ForeignKey(User, related_name='changed_mcfcarcolors', on_delete=models.CASCADE)
    isdeleted = models.BooleanField()

    class Meta:
        db_table = 'mcfcarcolor'

    def get_z_avtocolor(self):
        return z_avtocolor.objects.get(ColorID=self.idbs)






# Create your models here.
