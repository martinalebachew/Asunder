from utils.fs import *
from utils.logging import *

def check_prerequisites(prequisites):
  for (exec, name) in prequisites:
    if exec_path(exec) is None:
      print_error(f"Unfulfilled prerequisite: {name}")
      exit()
  
  print_success("All prerequisites fulfilled")
