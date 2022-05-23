import re
from django.shortcuts import render
from Tasker.settings import BASE_DIR
# Create your views here.
def main_view(request):
    return render(request,'index.html')