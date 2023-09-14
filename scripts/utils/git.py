from utils.shell import run_shell
from utils.logging import *

COMMIT_HASH_LENGTH = 40
SHORT_COMMIT_HASH_LENGTH = 7


def clone(github_specifier, path, branch=None, shallow=False):
  url = f"https://github.com/{github_specifier}"

  git_command = f"git clone {url} {path}"
  git_command += " --progress"
  git_command += f" --branch {branch}" if branch else ""
  git_command += " --depth 1" if shallow else ""
  _, output = run_shell(git_command)
  
  if output.endswith("done.\n"):
    print_success(f"Cloned {url} -> {path}")
  else:
    print_error(f"Failed to clone {url} -> {path}")
    exit()


def fetch_remote():
  git_command = "git fetch"
  return_code, _ = run_shell(git_command)

  if return_code != 0:
    print_error(f"Failed to fetch remote")
    exit()

  
def __commit_hash_impl(git_command):
  _, output = run_shell(git_command)
  output = output.strip()

  if len(output) == COMMIT_HASH_LENGTH:
    return output
  else:
    print_error(f"Failed to parse commit hash!")
    exit()


def local_last_commit_hash():
  git_command = "git rev-parse HEAD"
  return __commit_hash_impl(git_command)


def remote_last_commit_hash():
  fetch_remote()
  git_command = "git rev-parse origin"
  return __commit_hash_impl(git_command)
