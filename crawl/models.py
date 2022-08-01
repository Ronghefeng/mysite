from django.db import models
from asgiref.sync import sync_to_async


class BaseKurs(models.Model):
    harga_jual = models.DecimalField(max_digits=12, decimal_places=2)
    harga_beli = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_dan_waktu = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Dinar(BaseKurs):
    def __str__(self) -> str:
        return f"Dinar: {self.harga_jual}"


class Dirham(BaseKurs):
    def __str__(self) -> str:
        return f"Dirham: {self.harga_jual}"


# 将同步代码改为异步代码

dinar_get_all = sync_to_async(Dinar.objects.all)
dinar_create = sync_to_async(Dinar.objects.create)

dirham_get_all = sync_to_async(Dirham.objects.all)
dirham_create = sync_to_async(Dirham.objects.create)

# 民宿爬虫相关模型
class House(models.Model):
    pass


class Host(models.Model):
    pass


class Labels(models.Model):
    pass


class Facility(models.Model):
    pass


class City(models.Model):
    pass
