import os
import sys
import time
import requests

# Replace with your GitHub repository details
github_repo_owner = "HayatSiddique"
github_repo_name = "update"
local_version = "1.0.2"  # The current version of your self_update script
github_token = "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"  # Replace with your personal access token

def check_for_updates():
    try:
        url = f"https://api.github.com/repos/{github_repo_owner}/{github_repo_name}/releases/latest"
        headers = {"Authorization": f"token {github_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for any HTTP error

        latest_release = response.json()
        latest_version = latest_release["tag_name"]

        if latest_version != local_version:
            print(f"An update is available (v{latest_version}). Updating...")
            update_script()
        else:
            print("Self-update script is up to date.")
    except Exception as e:
        print(f"Error while checking for updates: {e}")

def update_script():
    try:
        url = f"https://github.com/{github_repo_owner}/{github_repo_name}/releases/latest/download/self_update.py"
        response = requests.get(url)
        response.raise_for_status()
        
        with open(__file__, "wb") as file:
            file.write(response.content)

        print("Self-update successful. Relaunching...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    except Exception as e:
        print(f"Error while updating script: {e}")

if __name__ == "__main__":
    while True:
        check_for_updates()
        time.sleep(600)  # Sleep for 10 minutes (600 seconds)
