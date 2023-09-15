import platform
from os.path import join
from utils.logging import *
from utils.fs import *
from utils.git import *
from utils.download import *
from utils.archives import *

os = platform.system()
arch = platform.machine()

pdfnetc_mirror = lambda version: f"https://raw.githubusercontent.com/martinalebachew/Asunder/mirror/pdfnetc/{version}.zip"


def determine_version():
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
  try:
    remove_directory(dependencies_dir)
    create_directory(dependencies_dir)

    version = determine_version()
    archive_path = f"{join(dependencies_dir, version)}.zip"
    pdfnetc_dir = join(dependencies_dir, "PDFNetC")

    download(pdfnetc_mirror(version), archive_path)
    shutil.unpack_archive(archive_path, pdfnetc_dir)
    remove_file(archive_path, ignore_file_not_found=False)

    print_success("Downloaded PDFNetC")

  except:
    print_error("Failed to download PDFNetC")
    exit()
