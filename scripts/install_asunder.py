from compile_decryptor import *
from build_extension import *
from utils.prerequisites import *
from shared.prerequisites import *

def install_asunder():
  check_prerequisites(installation_prerequisites)


if __name__ == "__main__":
  print("Compiling decryptor...")
  compile_decryptor()

  print("\nBuilding extension...")
  build_extension()

  print("\nInstalling Asunder...")
  install_asunder()
