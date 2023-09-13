import platform
from os.path import join
from utils.logging import *
from utils.fs import *
from utils.git import *

platform = platform.system()
arch = platform.machine()


def determine_source():
  if arch not in ["AMD64", "arm64"]:
    print_error(f"Unsupported architecture: {arch}")
    exit()

  if platform == "Linux" and arch == "AMD64":
    return "Linux-x64"
  elif platform == "Linux" and arch == "arm64":
    return "Linux-arm64"
  elif platform == "Windows":
    return "Windows-x64"
  elif platform == "Darwin":
    return "macOS-universal"
  else:
    print_error(f"Unsupported platform: {platform}")
    exit()


def get_pdfnetc(target_path):
  remove_directory(target_path)

  temp_dir = join(target_path, "temp")
  source_dir = join(temp_dir, determine_source())
  
  clone("martinalebachew/PDFNetC", temp_dir)
  move(source_dir, target_path)

  remove_directory(temp_dir)