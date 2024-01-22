"""1. Get the file path from the user, load and display the data"""
import sys
import os


file_path = sys.argv[1]

print(f"File path:", file_path)

if not os.path.exists(file_path):
    print(f"The path does not exist: {file_path}")
    print(f"Available files:")
    for fn in os.listdir():
      if fn.endswith(".py") or os.path.isdir(fn):
          continue
      print(f" - {fn}")  
else:
    with open(file_path, "r") as f:
        print("File opened!")