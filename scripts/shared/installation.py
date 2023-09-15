import platform
from utils.fs import resolve_path

os = platform.system()
installation_dir = r"/usr/local/etc/Asunder" if os != "Windows" else r"%PROGRAMFILES%\Asunder"
installation_dir = resolve_path(installation_dir)
