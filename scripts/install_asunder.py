import json, platform
from hashlib import sha256
from os.path import join
from compile_decryptor import *
from build_extension import *
from utils.fs import *
from utils.prerequisites import *
from utils.shell import *
from utils.logging import *
from shared.prerequisites import *
from shared.installation import *

os = platform.system()

def normalize_path(path):
  if os == "Windows" and path[0].islower() and path[1] == ':':
    return path[0].upper() + path[1:]

  return path


def encode_path(path):
  path = normalize_path(path)
  path_bytes = path.encode("utf-8" if os != "Windows" else "utf-16-le")
  return path_bytes


def get_extension_id(path):
  path_bytes = encode_path(path)
  id = sha256(path_bytes).hexdigest()[:32]
  id = ''.join([chr(int(digit, base=16) + ord('a')) for digit in id])
  return id


def register_native_host_manifest(extension_id):
  decryptor_file = "decryptor.exe" if os == "Windows" else "decryptor"
  decryptor_path = join(installation_dir, "decryptor", decryptor_file)

  manifest = {
    "name": native_host_identifier,
    "description": "Asunder Decryptor",
    "path": decryptor_path,
    "type": "stdio",
    "allowed_origins": [f"chrome-extension://{extension_id}/"]
  }

  manifest = json.dumps(manifest, indent=2)

  create_directory(native_host_manifest_dir)
  with open(native_host_manifest_path, "w") as manifest_file:
    manifest_file.write(manifest)

  print_success("Created native host manifest")

  if os == "Windows":
    return_code, _ = run_shell(windows_registry_command)

    if return_code == 0:
      print_success("Added native host to the registry")
    else:
      print_error("Failed to add native host to the registry")
      exit()


def install_asunder():
  check_prerequisites(installation_prerequisites)
  remove_directory(installation_dir)
   
  binaries_dir = join(get_decryptor_dir(), "bin")
  decryptor_installation_dir = join(installation_dir, "decryptor")

  dist_dir = join(get_extension_dir(), "dist")
  extension_installation_dir = join(installation_dir, "extension")

  copy_directory(binaries_dir, decryptor_installation_dir, ignore_file_not_found=False)

  extension_id = get_extension_id(extension_installation_dir)
  register_native_host_manifest(extension_id)
  copy_directory(dist_dir, extension_installation_dir, ignore_file_not_found=False)

  print_success("\nInstalled Asunder")
  print("Add the extension to Chrome manually by going to chrome://extensions")
  print(f"Enable Developer mode, click on Load unpacked, and navigate to {extension_installation_dir}")


if __name__ == "__main__":
  print("Compiling decryptor...")
  compile_decryptor()

  print("\nBuilding extension...")
  build_extension()

  print("\nInstalling Asunder...")
  install_asunder()
