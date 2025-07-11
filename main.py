# main.py
with open("notes.txt", "w") as f:
    f.write("This is my notes file.")


import os
import shutil

# Ensure .kaggle directory exists
os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)

# Copy credentials to the correct location
shutil.copy("kaggle.json", os.path.expanduser("~/.kaggle/kaggle.json"))

#Set permissions
os.chmod(os.path.expanduser("~/.kaggle/kaggle.json"), 0o600)
