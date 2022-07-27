from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm


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
    pass
