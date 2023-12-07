import requests
from datetime import datetime, timedelta

def get_new_commits(username, repository, token, since):
    url = f'https://api.github.com/repos/{username}/{repository}/commits'
    headers = {'Authorization': f'token {token}'}
    params = {'since': since}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        commits = response.json()
        file_path = "D:\Python\GIT\git_assignment_HeroVired\CI-CD-PIPELINE"
        with open(file_path, "w"):
          pass
        return commits
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")
        return None

def main():
    username = 'anarayana04'
    repository = 'git_assignment_HeroVired'
    token = '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'
    
    # Set the datetime for the last check (e.g., one day ago)
    since_datetime = (datetime.now() - timedelta(days=3)).isoformat()

    commits = get_new_commits(username, repository, token, since_datetime)

    if commits:
        print(f"New commits in {username}/{repository}:")
        for commit in commits:
            print(f"Commit: {commit['sha'][:7]} by {commit['commit']['author']['name']}: {commit['commit']['message']}")
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()