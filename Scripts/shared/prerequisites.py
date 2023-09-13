from sys import platform
from utils.logging import *

# (executable, readable_name)

shared_prerequisites = [
  ("cmake", "CMake"),
  ("vcpkg", "vcpkg"),
]

windows_prerequisites = shared_prerequisites + [
  ("MSBuild", "Visual Studio C++ Build Tools"),
]

macos_prerequisites = shared_prerequisites + [
  ("make", "GNU Make"),
  ("clang", "LLVM Clang"),
]

linux_prerequisites = shared_prerequisites + [
  ("make", "GNU Make"),
  ("gcc", "GNU Compiler Collection"),
]

def get_prerequisites():
  match platform:
    case "win32":
      return windows_prerequisites
    case "darwin":
      return macos_prerequisites
    case "linux":
      return linux_prerequisites
    case _:
      print_error(f"Unsupported platform: {platform}")
      exit()

