from django.shortcuts import render
from . import psutil_utils

def index(request):
    cpu = psutil_utils.get_cpu_percent(interval=0.1)
    mem = psutil_utils.get_memory_info()
    disk = psutil_utils.get_disk_info('/')
    sysinfo = psutil_utils.get_system_info()

    # Convertir bytes a GB
    if mem:
        mem['used_gb'] = psutil_utils.bytes_to_gb(mem['used'])
        mem['total_gb'] = psutil_utils.bytes_to_gb(mem['total'])
    if disk:
        disk['used_gb'] = psutil_utils.bytes_to_gb(disk['used'])
        disk['total_gb'] = psutil_utils.bytes_to_gb(disk['total'])
        disk['free_gb'] = psutil_utils.bytes_to_gb(disk['free'])

    context = {
        'cpu_percent': cpu,
        'mem': mem,
        'disk': disk,
        'sysinfo': sysinfo,
    }
    return render(request, 'sistema/index.html', context)