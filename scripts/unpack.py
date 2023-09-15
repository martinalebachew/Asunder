import shutil, os
from os.path import dirname, join, isfile
from glob import glob

zip_extension = ".zip"

def unpack():
  scripts_dir = dirname(__file__)
  root_dir = dirname(scripts_dir)

  for file_path in glob(join(root_dir, f"*{zip_extension}")):
    if isfile(file_path):
      output_dir = file_path[:-len(zip_extension)]
      shutil.unpack_archive(file_path, output_dir)
      os.remove(file_path)

      print(f"Unpacked {file_path}")


if __name__ == "__main__":
  unpack()
