import subprocess
import time

def get_latest_commit_hash():
    command = "git log -n 1 --pretty=format:%H"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def main():
    repository_url = "https://github.com/your-username/your-repo.git"
    current_commit = None

    while True:
        latest_commit = get_latest_commit_hash()

        if latest_commit != current_commit:
            print("New commit detected. Deploying code...")
            subprocess.run(["./deploy.sh", repository_url])
            current_commit = latest_commit

        time.sleep(60)  # Check every minute (adjust as needed)

if __name__ == "__main__":
    main()