import os
import sys
import urllib.request
import zipfile
import getpass
import shutil

def install():
    user_folder = os.path.expanduser("~")
    tools_folder = os.path.join(user_folder, "ncat_tool")
    os.makedirs(tools_folder, exist_ok=True)

    zip_url = "https://nmap.org/dist/ncat-portable-5.59BETA1.zip"
    zip_path = os.path.join(tools_folder, "ncat.zip")

    print(f"Downloading Ncat to {zip_path}…")
    urllib.request.urlretrieve(zip_url, zip_path)
    print("Download completed")

    with zipfile.ZipFile(zip_path, "r") as z:
        for member in z.namelist():
            if member.endswith("ncat.exe"):
                print("Extracting ncat.exe…")
                z.extract(member, tools_folder)
                src = os.path.join(tools_folder, member)
                dst = os.path.join(tools_folder, "ncat.exe")
                shutil.move(src, dst)
                break

    os.remove(zip_path)
    print(f"Ncat is ready at {dst}")

    
    os.environ["PATH"] = tools_folder + os.pathsep + os.environ.get("PATH", "")
    return dst

if __name__ == "__main__":
    ncat_path = install()
    print(f"Invoke Ncat via: {ncat_path}")
