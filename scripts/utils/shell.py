from subprocess import Popen, PIPE, STDOUT
from utils.logging import *

def run_shell(command, cwd=None, bytes=False):
  process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, text=(not bytes), cwd=cwd)
  stdout, stderr = process.communicate()

  divider = b"\n" if stdout and stderr else b""
  stdout = stdout if stdout else b""
  stderr = stderr if stderr else b""

  divider = divider if bytes else str(divider)
  stdout = stdout if bytes else str(stdout)
  stderr = stderr if bytes else str(stderr)

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
