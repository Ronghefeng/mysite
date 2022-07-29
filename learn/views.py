from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
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
