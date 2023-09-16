import platform
from utils.fs import resolve_path

os = platform.system()
installation_dir = r"~/.asunder" if os != "Windows" else r"~\.asunder"
installation_dir = resolve_path(installation_dir)
