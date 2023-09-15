import shutil
from os.path import dirname, join, isdir, basename
from glob import glob

def pack():
  scripts_dir = dirname(__file__)
  root_dir = dirname(scripts_dir)

  for dir_path in glob(join(root_dir, "*")):
    if isdir(dir_path) and dir_path != scripts_dir:
      output_file = join(root_dir, basename(dir_path))
      shutil.make_archive(output_file, "zip", dir_path)
      shutil.rmtree(dir_path)

      print(f"Packed {dir_path}")


if __name__ == "__main__":
  pack()
