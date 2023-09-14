from os.path import join, dirname
from utils.shell import *
from utils.node import *
from utils.prerequisites import *
from shared.prerequisites import *

def get_extension_dir():
  scripts_dir = dirname(__file__)
  project_root = dirname(scripts_dir)
  decryptor_dir = join(project_root, "extension")
  return decryptor_dir


def run_build_script(extension_dir):
  return_code, _ = run_shell("npm run build", cwd=extension_dir)
  if return_code == 0:
    print_success("Built extension")
  else:
    print_error("Failed to build extension")
    exit()
  

def build_extension():
  check_prerequisites(extension_prerequisites)
  extension_dir = get_extension_dir()
  install_packages(extension_dir)
  run_build_script(extension_dir)


if __name__ == "__main__":
  build_extension()
