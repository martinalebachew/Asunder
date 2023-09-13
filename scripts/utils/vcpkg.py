import platform
from utils.logging import *
from utils.shell import *
from shared.vcpkg import *

def get_installed_packages(triplets=False):
  _, output = run_shell("vcpkg list")
  packages = []

  for line in output.splitlines():
    divider_index = line.find(" " if triplets else ":")
    if divider_index != -1:
      packages.append(line[:divider_index])
    else:
      print_error("Failed to parse vcpkg packages")
      exit()

  return packages


def check_packages():
  # Windows requires explicit x64-windows triplets
  # vcpkg releases before September 2023 default to x86 on Windows
  is_windows = platform.system() == "Windows"
  installed = get_installed_packages(triplets=is_windows)
  for required in required_packages:
    required += ":x64-windows" if is_windows else ""
    if required not in installed:
      print_error(f"vcpkg package {required} not installed")
      exit()


def get_cmake_toolchain_flag():
  _, output = run_shell("vcpkg integrate install")
  for line in output.splitlines():
    if line.startswith("CMake projects should use: "):
      return line.split(":")[1].strip()
    
  print_error("Failed to parse vcpkg CMake toolchain flag")
  exit()
