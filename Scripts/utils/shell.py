from subprocess import Popen, PIPE, STDOUT
from utils.logging import *

def run_shell(command):
  process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
  return_code = process.wait()
  output = process.stdout.read()
  return (return_code, output)


def run_script(path):
  return_code, output = run_shell(path)
  if return_code == 0:
    print_success(f"Ran script {path}")
  else:
    print_error(f"Failed to run script {path}")
    exit()

  return output
