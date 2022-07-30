import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from . import models


def index(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render(request, "sys_cache/index.html", locals())


class UploadView(View):
    def get(self, request):

        return render(request, "sys_cache/upload.html")

    def post(self, request):

        desc = request.POST.get("desc", "")

        name = request.POST.get("name", "")

        shop = models.Shop(name=name, desc=desc)

        shop.save()

        img_list = request.FILES.getlist("img")

        images = []

        for img in img_list:

            images.append(models.Img(img=img, name=shop, img_type=1))

        models.Img.objects.bulk_create(images)

        return HttpResponse("Upload success!")
