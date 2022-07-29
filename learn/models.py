from django.urls import reverse
import os
from django.db import models
from datetime import date
from uuid import uuid4
from django.conf import settings


class Document(models.Model):
    # 使用模型表单
    document = models.FileField(upload_to="documents/%Y/%m/%d")
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Person(models.Model):
    name = models.CharField(max_length=50)
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True)

    class Meta:
        abstract = True


class Employee(Person):
    joint_date = models.DateField()


class Customer(Person):
    first_name = models.CharField(max_length=50)
    dirth_day = models.DateField()


class OrderEmployee(Employee):
    class Meta:
        ordering = ["-joint_date"]
        proxy = True

    @property
    def work_id(self):
        return f"{self.name}:{self.id}"


class Picture(models.Model):

    title = models.CharField(max_length=20, blank=True, default="")

    image = models.ImageField(upload_to="mypictures", blank=True)

    date = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        # 对象编辑或者创建后的返回地址
        return reverse("learn:pic_detail", args=[str(self.id)])
