import shutil, os
from utils.logging import *

def remove_directory(path, ignore_file_not_found=True):
  __remove_impl(path, ignore_file_not_found, directory=True)


def remove_file(path, ignore_file_not_found=True):
  __remove_impl(path, ignore_file_not_found, directory=False)


def __remove_impl(path, ignore_file_not_found, directory):
  try:
    if directory:
      shutil.rmtree(path)
    else:
      os.remove(path)

    print_success(f"Removed {path}")

  except Exception as error:
    if isinstance(error, FileNotFoundError) and ignore_file_not_found:
      print_notice(f"Skipped removing {path}")
    else:
      print_error(f"Failed to remove {path}")
      exit()


def move(source, destination, ignore_file_not_found=True):
  try:
    shutil.move(source, destination)
    print_success(f"Moved {source} -> {destination}")

  except Exception as error:
    if isinstance(error, FileNotFoundError) and ignore_file_not_found:
      print_notice(f"Skipped moving {source} -> {destination}")
    else:
      print_error(f"Failed to move {source} -> {destination}")
      exit()


def copy_file(source, destination, ignore_file_not_found=True):
  try:
    shutil.copyfile(source, destination)
    print_success(f"Copied {source} -> {destination}")

  except Exception as error:
    if isinstance(error, FileNotFoundError) and ignore_file_not_found:
      print_notice(f"Skipped copying {source} -> {destination}")
    else:
      print_error(f"Failed to copy {source} -> {destination}")
      exit()


def resolve_path(path):
  return path.replace("~", os.path.expanduser("~"))


def exec_path(exec_name):
  return shutil.which(exec_name)
