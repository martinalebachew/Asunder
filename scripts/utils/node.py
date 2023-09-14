from utils.shell import *

def install_packages(extension_dir):
  return_code, _ = run_shell("npm install", cwd=extension_dir)
  
  if return_code == 0:
    print_success("Installed Node.js packages")
  else:
    print_error("Failed to install Node.js packages")
    exit()
