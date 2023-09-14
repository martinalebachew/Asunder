from utils.fs import *
from utils.logging import *
from shared.prerequisites import *

def check_prerequisites():
  for (exec, name) in get_prerequisites():
    if exec_path(exec) is None:
      print_error(f"Unfulfilled prerequisite: {name}")
      exit()
  
  print_success("All prerequisites fulfilled")
