from subprocess import Popen, PIPE, STDOUT
from utils.logging import *

def run_shell(command, cwd=None):
  process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, text=True, cwd=cwd)
  stdout, stderr = process.communicate()

  divider = "\n" if stdout and stderr else ""
  stdout = stdout if stdout else ""
  stderr = stderr if stderr else ""
  output = stdout + divider + stderr
  return (process.returncode, output)


def run_script(path):
  return_code, output = run_shell(path)
  if return_code == 0:
    print_success(f"Ran script {path}")
  else:
    print_error(f"Failed to run script {path}")
    exit()

  return output
