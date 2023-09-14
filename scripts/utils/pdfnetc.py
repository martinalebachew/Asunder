import platform
from os.path import join
from utils.logging import *
from utils.fs import *
from utils.git import *

os = platform.system()
arch = platform.machine()


def determine_source():
  if arch not in ["AMD64", "arm64"]:
    print_error(f"Unsupported architecture: {arch}")
    exit()

  if os == "Linux" and arch == "AMD64":
    return "Linux-x64"
  elif os == "Linux" and arch == "arm64":
    return "Linux-arm64"
  elif os == "Windows":
    return "Windows-x64"
  elif os == "Darwin":
    return "macOS-universal"
  else:
    print_error(f"Unsupported OS: {os}")
    exit()


def get_pdfnetc(dependencies_dir):
  remove_directory(dependencies_dir)
  temp_dir = join(dependencies_dir, "tmp")
  source_dir = join(temp_dir, determine_source())
  pdfnetc_dir = join(dependencies_dir, "PDFNetC")

  clone("martinalebachew/PDFNetC", temp_dir, shallow=True)
  move(source_dir, pdfnetc_dir, ignore_file_not_found=False)
  remove_directory(temp_dir)

  print_success("Downloaded PDFNetC")
