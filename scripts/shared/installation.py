import platform
from os.path import join
from utils.fs import resolve_path
from utils.logging import *

os = platform.system()
installation_dir = r"~/.asunder" if os != "Windows" else r"~\.asunder"
installation_dir = resolve_path(installation_dir)


native_host_identifier = "com.martinalebachew.asunder"
native_host_filename = f"_{native_host_identifier}_.json"

def get_native_host_manifest_dir():
  if os == "Windows":
    return join(installation_dir, native_host_filename)
  elif os == "Darwin":
    return "~/.config/google-chrome/NativeMessagingHosts"
  elif os == "Linux":
    return "~/Library/Application Support/Google/Chrome/NativeMessagingHosts"
  else:
    print_error(f"Unsupported OS: {os}")
    exit()


native_host_manifest_path = join(get_native_host_manifest_dir(), native_host_filename)
