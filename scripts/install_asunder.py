from compile_decryptor import *
from build_extension import *
from utils.prerequisites import *
from shared.prerequisites import *

def build_all():
  compile_decryptor()
  build_extension()


def install_asunder():
  check_prerequisites(installation_prerequisites)


if __name__ == "__main__":
  build_all()
  install_asunder()
