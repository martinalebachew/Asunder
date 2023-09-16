from subprocess import Popen, PIPE, STDOUT
from utils.logging import *

def run_shell(command, cwd=None, bytes=False):
  process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, text=(not bytes), cwd=cwd)
  stdout, stderr = process.communicate()

  empty_string = b"" if bytes else ""
  newline_char = b"\n" if bytes else "\n"

  stdout = stdout if stdout else empty_string
  stderr = stderr if stderr else empty_string

  divider = newline_char if stdout and stderr else empty_string
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
