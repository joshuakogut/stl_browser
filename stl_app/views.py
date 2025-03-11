from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import os


def list_stl_files(request):
    stl_files_dir = settings.STL_FILES_DIR
    try:
        files = [f for f in os.listdir(stl_files_dir) if f.endswith(".stl")]
    except FileNotFoundError:
        files = []
    return render(request, "stl_files_list.html", {"stl_files": files})


def stl_viewer(request, filename):
    return render(request, "stl_viewer.html", {"filename": filename})
