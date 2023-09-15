from urllib.request import urlretrieve
from utils.logging import *

def download(url, filename):
  try:
    urlretrieve(url, filename)
    print_success(f"Downloaded {url} -> {filename}")

  except:
    print_error(f"Failed to download {url} -> {filename}")
    exit()
