from os.path import join, dirname
def get_extension_dir():
  scripts_dir = dirname(__file__)
  project_root = dirname(scripts_dir)
  decryptor_dir = join(project_root, "extension")
  return decryptor_dir
