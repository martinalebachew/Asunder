from os.path import join, dirname
from utils.shell import *

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
