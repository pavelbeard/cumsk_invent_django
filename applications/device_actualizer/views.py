import re

from django.shortcuts import render, redirect
from rest_framework import status
from cumsk_invent_django.extentions import Extentions

from cumsk_invent_django.extentions import *
from . import models
from .forms import *
from asgiref.sync import sync_to_async

# Create your views here.


# region SNMPc section
def snmpc_devices_view(request):
    snmpc_devices = models.Nodetable.objects.all()
    url = request.get_full_path()
    return render(
        request,
        'device_actualizer/snmpc_devices.html',
        {'snmpc_devices': snmpc_devices})


def snmpc_devices_view_filter(request, filter):
    match filter:
        case 'cutk':
            snmpc_devices = models.Nodetable.objects.filter(address__contains='10.190')
            return render(
                request,
                'device_actualizer/snmpc_devices.html',
                {'snmpc_devices': snmpc_devices}
            )
        case 'css':
            pass


def snmpc_device_view(request, dev_snmpc_id):
    id = re.search(r'(.*\_){3}(.*)', dev_snmpc_id).group(2)
    snmpc_device = models.Nodetable.objects.filter(node_id=id)
    model_fields = snmpc_device.model._meta.fields
    model_values = [str(value) for value in dict(snmpc_device.values().first()).values()]
    return render(
        request,
        'device_actualizer/snmpc_device_detail.html',
        {
            'id': id,
            'snmpc_device_fields': model_fields,
            'snmpc_device_values': model_values,
        }
    )


# endregion
# region ESMA section
def esma_devices_view(request):
    esma_devices = models.CiscoDs.objects.all()
    return render(request, 'device_actualizer/esma_devices.html', {'esma_devices': esma_devices})


def esma_device_view(request, dev_esma_id):
    id = int(re.search(r'(.*\_){3}(.*)', dev_esma_id).group(2))
    esma_device = models.CiscoDs.objects.filter(id=id)
    model_fields = esma_device.model._meta.fields
    model_values = [str(value) for value in dict(esma_device.values().first()).values()]
    return render(
        request,
        'device_actualizer/esma_device_detail.html',
        {
            'id': id,
            'esma_device_fields': model_fields,
            'esma_device_values': model_values,
        }
    )


# endregion

# region Upload file
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                ext = Extentions()
                return ext.handle_upload_file(file, request.get_full_path(), redirect)
            except BaseException:
                error_text = 'Ошибка при обработке файла'
                return redirect('applications.device_actualizer:error')
    else:
        form = UploadFileForm()
    return render(request, 'device_actualizer/upload.html', {'form': form})


# endregion

# region Error section
def error(request, error_text):
    return render(
        request,
        template_name='device_actualizer/error.html',
        status=status.HTTP_501_NOT_IMPLEMENTED,
        context=error_text
    )
# endregion
