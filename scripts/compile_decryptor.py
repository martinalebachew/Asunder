import platform
from os.path import join, dirname
from utils.fs import *
from utils.vcpkg import *
from utils.pdfnetc import *
from utils.prerequisites import *
from shared.prerequisites import *

def get_decryptor_dir():
  scripts_dir = dirname(__file__)
  project_root = dirname(scripts_dir)
  decryptor_dir = join(project_root, "decryptor")
  return decryptor_dir


def get_dependencies_dir():
  decryptor_dir = get_decryptor_dir()
  dependencies_dir = join(decryptor_dir, "dep")
  return dependencies_dir


def get_build_dir():
  decryptor_dir = get_decryptor_dir()
  build_dir = join(decryptor_dir, "build")
  return build_dir


def configure_build():
  cmake_command = "cmake .."
  if platform.system() == "Windows":
    cmake_command += " -A x64"

  cmake_command += f" {get_cmake_toolchain_flag()}"
  build_dir = get_build_dir()
  remove_directory(build_dir)
  create_directory(build_dir)
  return_code, _ = run_shell(cmake_command, cwd=build_dir)
  
  if return_code == 0:
    print_success("Configured build using CMake")
  else:
    print_error("Failed to configure build using CMake")
    exit()


def build_executable():
  cmake_command = "cmake --build ."
  if platform.system() == "Windows":
    cmake_command += " --config Release"

  build_dir = get_build_dir()
  return_code, _ = run_shell(cmake_command, cwd=build_dir)
  
  if return_code == 0:
    print_success("Built decryptor")
  else:
    print_error("Failed to build decryptor")
    exit()


def compile_decryptor():
  check_prerequisites(decryptor_prerequisites)
  check_packages()
  get_pdfnetc(get_dependencies_dir())
  configure_build()
  build_executable()


if __name__ == "__main__":
  compile_decryptor()
