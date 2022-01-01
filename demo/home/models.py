from django.db import models

# Create your models here.
class danhmucsanpham(models.Model):
    danhmucsanpham_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.danhmucsanpham_id},{self.name}"
        