import os
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView
from django.http import FileResponse, Http404, HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from .models import Document, Picture
from .forms import DocumentForm, AddForm


def home(request):
    documents = Document.objects.all()
    return render(request, "learn/home.html", {"documents": documents})


def simple_upload(request):
    if request.method == "POST" and request.FILES["myfile"]:
        myfile = request.FILES["myfile"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(filename)
        return render(
            request, "learn/simple_upload.html", {"upload_file_url": upload_file_url}
        )

    return render(request, "learn/simple_upload.html")


def model_form_upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("learn:home")

    else:
        form = DocumentForm()
    return render(request, "learn/model_form_upload.html", {"form": form})


# 文件下载
class DownLoadView:

    FILE_URL = os.path.join(settings.MEDIA_ROOT, "mypictures")
    DOWNLOAD_PIC = "liuyifei2.jpg"
    DOWNLOAD_FILE = "test_download_file.txt"
    DOWNLOAD_CSV_FILE = "test_download_csv.csv"

    def download_pic_method_1(self, request):
        # 使用 open 打开文件读取内容返回，此方式不适合大型文件，容易占用较多内存

        with open(os.path.join(self.FILE_URL, self.DOWNLOAD_FILE)) as f:
            file_c = f.read()

        # 显示图片：
        import base64

        with open(os.path.join(self.FILE_URL, self.DOWNLOAD_PIC), "rb") as f:
            c = f.read()
            img_stream = base64.b64encode(c).decode()

        # 需要注意前段展示不同图片类型，src 的内容有区别
        return HttpResponse(
            f'<img style="width:180px" src="data:image/jpg;base64,{img_stream}"><br><h1>{file_c}</h1>'
        )

    def download_pic_method_2(self, request):
        # 使用 HttpResonse 下载，适合 txt 小文件，不适合大的二进制文件
        # 直接浏览器访问地址下载文件到本地机器

        filepath = os.path.join(self.FILE_URL, self.DOWNLOAD_FILE)
        with open(filepath) as f:
            try:
                response = HttpResponse(f)
                response["content_type"] = "application/octet-stream"
                response[
                    "Content-Disposition"
                ] = "attachment; filename=" + os.path.basename(filepath)
                return response
            except Exception:
                raise Http404

    def download_pic_method_3(self, request):
        # 使用 StreamingHttpResponse 下载，适合流式传输的大型文件，例如 csv 等

        file_path = os.path.join(self.FILE_URL, self.DOWNLOAD_CSV_FILE)

        try:
            response = StreamingHttpResponse(open(file_path, "rb"))
            response["content_type"] = "application/octet-stream"
            response[
                "Content-Disposition"
            ] = "attachment; filename=" + os.path.basename(file_path)
            return response
        except Exception:
            raise Http404

    def download_pic_method_4(self, request):
        # 使用 FileResponse 下载，适合大文件

        file_path = os.path.join(self.FILE_URL, self.DOWNLOAD_CSV_FILE)

        try:
            response = FileResponse(open(file_path, "rb"))
            response["content_type"] = "application/octet-stream"
            response[
                "Content-Disposition"
            ] = "attachment; filename=" + os.path.basename(file_path)
            return response
        except Exception:
            raise Http404

    def download_pic(self, request):
        return self.download_pic_method_4(request)


def add_view(request):

    if request.method.lower() == "post":

        form = AddForm(request.POST)

        if form.is_valid():  # 检查 form 表单中的数据是否有效，有效的数据会保存到 cleaned_data 中

            numb1 = form.cleaned_data["numb1"]
            numb2 = form.cleaned_data["numb2"]

            return HttpResponse(str(int(numb1) + int(numb2)))
    else:
        form = AddForm()  # 当 get 请求时返回空表单，否则返回当前填入数据的表单

    return render(request, "learn/add_form.html", {"form": form})


class Piclist(ListView):

    queryset = Picture.objects.all().order_by("-date")


class PicDetail(DetailView):

    model = Picture


class PicUpload(CreateView):

    model = Picture

    fields = ("title", "image")
