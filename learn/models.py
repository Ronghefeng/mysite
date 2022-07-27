from django.db import models


class Document(models.Model):
    # 使用模型表单
    document = models.FileField(upload_to="documents/%Y/%m/%d")
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
