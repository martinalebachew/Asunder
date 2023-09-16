from utils.shell import *
from utils.logging import *

def generate_keyfile(filename="key.pem"):
  return_code, _ = run_shell(f"openssl genrsa 2048 | openssl pkcs8 -topk8 -nocrypt -out \"{filename}\"")
  
  if return_code == 0:
    print_success(f"Generated keyfile {filename}")

  else:
    print_error(f"Failed to generate keyfile {filename}")
    exit()
