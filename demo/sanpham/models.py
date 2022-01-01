from django.db import models
from home.models import danhmucsanpham
# Create your models here.

class sanpham(models.Model):
    sanpham_id = models.AutoField(primary_key=True)
    danhmucsanpham_id = models.ForeignKey(danhmucsanpham, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=True)
    anh = models.ImageField(upload_to='images', null=False, default=None)
    mota = models.CharField(max_length=200000, null=False, default=None)

    def __str__(self):
        return f"{self.sanpham_id},{self.danhmucsanpham_id},{self.name},{self.price},{self.anh},{self.mota}"