import re
from django.shortcuts import render
from Tasker.settings import BASE_DIR
# Create your views here.
def main_view(request):
    print(BASE_DIR.parent)
    return render(request,'index.html')