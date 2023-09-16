import json, platform
from os.path import join
from compile_decryptor import *
from build_extension import *
from utils.fs import *
from utils.prerequisites import *
from utils.crypto import *
from shared.prerequisites import *
from shared.installation import *

def add_key_to_extension_manifest(key_field):
  dist_dir = join(get_extension_dir(), "dist")
  manifest_path = join(dist_dir, "manifest.json")

  with open(manifest_path, "r") as manifest_file:
    manifest = json.load(manifest_file)

  manifest["key"] = key_field

  with open(manifest_path, "w") as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

  print_success("Added key to manifest file")


def register_native_host_manifest(extension_id):
  os = platform.system()
  decryptor_file = "decryptor.exe" if os == "Windows" else "decryptor"
  decryptor_path = join(installation_dir, decryptor_file)

  manifest = {
    "name": native_host_identifier,
    "description": "Asunder Decryptor",
    "path": f"{decryptor_path}",
    "type": "stdio",
    "allowed_origins": [f"chrome-extension://{extension_id}/"]
  }

  manifest = json.dumps(manifest, indent=2)

  create_directory(native_host_manifest_dir)
  with open(native_host_manifest_path, "w") as manifest_file:
    manifest_file.write(manifest)

  print_success("Created native host manifest")


def install_asunder():
  check_prerequisites(installation_prerequisites)
  remove_directory(installation_dir)
 
  generate_keyfile()
  key_field = get_public_key()
  add_key_to_extension_manifest(key_field)
  
  binaries_dir = join(get_decryptor_dir(), "bin")
  copy_directory(binaries_dir, installation_dir, ignore_file_not_found=False)
 
  extension_id = get_extension_id()
  register_native_host_manifest(extension_id)


if __name__ == "__main__":
  print("Compiling decryptor...")
  compile_decryptor()

  print("\nBuilding extension...")
  build_extension()

  print("\nInstalling Asunder...")
  install_asunder()
