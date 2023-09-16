import json
from os.path import join
from compile_decryptor import *
from build_extension import *
from utils.fs import *
from utils.prerequisites import *
from utils.crypto import *
from shared.prerequisites import *
from shared.installation import *

def add_key_to_manifest(key_field):
  dist_dir = join(get_extension_dir(), "dist")
  manifest_path = join(dist_dir, "manifest.json")

  with open(manifest_path, "r") as manifest_file:
    manifest = json.load(manifest_file)

  manifest["key"] = key_field

  with open(manifest_path, "w") as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

  print_success("Added key to manifest file")


def install_asunder():
  check_prerequisites(installation_prerequisites)
  remove_directory(installation_dir)
 
  generate_keyfile()
  key_field = get_public_key()
  add_key_to_manifest(key_field)
 
  bin_dir = join(get_decryptor_dir(), "bin")
  copy_directory(bin_dir, installation_dir)


if __name__ == "__main__":
  print("Compiling decryptor...")
  compile_decryptor()

  print("\nBuilding extension...")
  build_extension()

  print("\nInstalling Asunder...")
  install_asunder()
