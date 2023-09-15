import shutil
from utils.logging import *

def unpack(archive_path, destination):
  try:
    shutil.unpack_archive(archive_path, destination)
    print_success(f"Unpacked {archive_path} -> {destination}")
  
  except:
    print_error(f"Failed to unpack {archive_path} -> {destination}")
    exit()
