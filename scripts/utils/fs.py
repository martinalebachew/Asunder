import shutil, os, stat
from utils.logging import *

def remove_readonly(func, path, _):
  # Change file permissions and reattempt the removal
  os.chmod(path, stat.S_IWRITE)
  os.remove(path)


def remove_directory(path, ignore_file_not_found=True):
  __remove_impl(path, ignore_file_not_found, directory=True)


def remove_file(path, ignore_file_not_found=True):
  __remove_impl(path, ignore_file_not_found, directory=False)


def __remove_impl(path, ignore_file_not_found, directory):
  try:
    if directory:
      shutil.rmtree(path, onerror=remove_readonly)
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


def __copy_impl(source, destination, ignore_file_not_found, directory):
  try:
    if directory:
      shutil.copytree(source, destination)
    else:
      shutil.copyfile(source, destination)

    print_success(f"Copied {source} -> {destination}")

  except Exception as error:
    if isinstance(error, FileNotFoundError) and ignore_file_not_found:
      print_notice(f"Skipped copying {source} -> {destination}")
    else:
      print_error(f"Failed to copy {source} -> {destination}")
      exit()


def copy_file(source, destination, ignore_file_not_found=True):
  __copy_impl(source, destination, ignore_file_not_found, directory=False)


def copy_directory(source, destination, ignore_file_not_found=True):
  __copy_impl(source, destination, ignore_file_not_found, directory=True)


def create_directory(path, ignore_file_exists=True):
  try:
    os.mkdir(path)
    print_success(f"Created directory {path}")

  except Exception as error:
    if isinstance(error, FileExistsError) and ignore_file_exists:
      print_notice(f"Skipped creating directory {path}")
    else:
      print_error(f"Failed to create directory {path}")
      exit()


def resolve_path(path):
  return os.path.expandvars(os.path.expanduser(path))


def exec_path(exec_name):
  return shutil.which(exec_name)
