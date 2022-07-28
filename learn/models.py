from django.db import models


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
