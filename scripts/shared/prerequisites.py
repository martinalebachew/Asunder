import platform
from utils.logging import *

# (executable, readable_name)

shared_prerequisites = [
  ("git-lfs", "Git LFS"),
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
  os = platform.system()
  match os:
    case "Windows":
      return windows_prerequisites
    case "Darwin":
      return macos_prerequisites
    case "Linux":
      return linux_prerequisites
    case _:
      print_error(f"Unsupported OS: {os}")
      exit()

