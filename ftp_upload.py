import os
from ftplib import FTP

FTP_SERVER = os.environ['FTP_SERVER']
FTP_USERNAME = os.environ['FTP_USERNAME']
FTP_PASSWORD = os.environ['FTP_PASSWORD']
LOCAL_DIR = os.environ['INPUT_LOCAL_DIR']
REMOTE_DIR = os.environ['INPUT_REMOTE_DIR']

def upload_files(ftp, local_dir, remote_dir):
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            remote_path = os.path.join(remote_dir, os.path.relpath(local_path, local_dir))
            remote_path = remote_path.replace("\\", "/")
            print(f"Uploading: {local_path} => {remote_path}")
            with open(local_path, 'rb') as f:
                ftp.storbinary(f"STOR {remote_path}", f)

def main():
    ftp = FTP(FTP_SERVER)
    ftp.login(FTP_USERNAME, FTP_PASSWORD)
    upload_files(ftp, LOCAL_DIR, REMOTE_DIR)
    ftp.quit()

if __name__ == "__main__":
    main()
