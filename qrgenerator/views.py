# Create your views here.
# qrcodeapp/views.py

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from pathlib import Path



def qrgenerator(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(Path(settings.MEDIA_ROOT) / img_name)
        return render(request, 'qrgenerator/index.html', {'img_name': img_name})
    return render(request, 'qrgenerator/index.html')