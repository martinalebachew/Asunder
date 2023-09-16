from utils.shell import *
from utils.logging import *
from base64 import b64encode
from hashlib import sha256

def generate_keyfile(filename="key.pem"):
  return_code, _ = run_shell(f"openssl genrsa 2048 | openssl pkcs8 -topk8 -nocrypt -out \"{filename}\"")

  if return_code == 0:
    print_success(f"Generated keyfile {filename}")

  else:
    print_error(f"Failed to generate keyfile {filename}")
    exit()


def __get_public_key_impl(filename="key.pem"):
  return_code, output = run_shell(f"openssl rsa -in {filename} -pubout -outform DER", bytes=True)

  if return_code == 0:
    print_success(f"Calculated public key from {filename}")
    public_key = output[output.find(b"\n") + 1:]
    return public_key

  else:
    print_error(f"Failed to calculate public key from {filename}")
    exit()


def get_public_key(filename="key.pem"):
  public_key = __get_public_key_impl(filename)
  return b64encode(public_key).decode()
  

def get_extension_id(filename="key.pem"):
  public_key_bytes = __get_public_key_impl(filename)
  id = sha256(public_key_bytes).hexdigest()[:32]
  id = id.translate(str.maketrans("0123456789abcdef", "abcdefghijklmnop"))
  return id
