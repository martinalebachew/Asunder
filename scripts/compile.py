from os.path import join, dirname
from utils.fs import *
from utils.vcpkg import *
from utils.prerequisites import *
from utils.pdfnetc import *

def get_dependencies_dir():
  scripts_dir = dirname(__file__)
  project_root = dirname(scripts_dir)
  decryptor_dir = join(project_root, "decryptor")
  dependencies_dir = join(decryptor_dir, "dep")
  return dependencies_dir


if __name__ == "__main__":
  check_prerequisites()
  check_packages()
  get_pdfnetc(get_dependencies_dir())
