import platform
from utils.fs import resolve_path

os = platform.system()
installation_dir = r"~/Asunder" if os != "Windows" else r"~\Asunder"
installation_dir = resolve_path(installation_dir)
