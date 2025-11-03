import platform

try:
    import psutil
    PSUTIL_AVAILABLE = True
except Exception:
    psutil = None
    PSUTIL_AVAILABLE = False

def get_cpu_percent(interval=0.5):
    if not PSUTIL_AVAILABLE:
        return None
    try:
        return psutil.cpu_percent(interval=interval)
    except Exception:
        return None

def get_memory_info():
    if not PSUTIL_AVAILABLE:
        return None
    try:
        vm = psutil.virtual_memory()
        return {
            'total': vm.total,
            'available': vm.available,
            'used': vm.used,
            'percent': vm.percent,
        }
    except Exception:
        return None

def get_disk_info(path='/'):
    if not PSUTIL_AVAILABLE:
        return None
    try:
        du = psutil.disk_usage(path)
        return {
            'total': du.total,
            'used': du.used,
            'free': du.free,
            'percent': du.percent,
        }
    except Exception:
        return None

def get_system_info():
    try:
        sysinfo = {
            'platform': platform.system(),
            'platform_release': platform.release(),
            'platform_version': platform.version(),
            'architecture': platform.machine(),
            'processor': platform.processor(),
            'cpu_logical': None,
            'cpu_physical': None,
            'psutil_available': PSUTIL_AVAILABLE,
        }
        if PSUTIL_AVAILABLE:
            try:
                sysinfo['cpu_logical'] = psutil.cpu_count(logical=True)
                sysinfo['cpu_physical'] = psutil.cpu_count(logical=False)
            except Exception:
                sysinfo['cpu_logical'] = None
                sysinfo['cpu_physical'] = None
        return sysinfo
    except Exception:
        return None

def bytes_to_gb(n_bytes):
    return round(n_bytes / (1024 ** 3), 2) if n_bytes is not None else None