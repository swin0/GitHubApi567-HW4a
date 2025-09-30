import requests

def get_user_repos_and_commits(user_id):
    base_url = "https://api.github.com"
    repos_url = f"{base_url}/users/{user_id}/repos"

    try:
        repos_response = requests.get(repos_url)
        repos_response.raise_for_status()
        repos_data = repos_response.json()

        repo_commit_info = []

        for repo in repos_data:
            repo_name = repo.get("name")
            commits_url = f"{base_url}/repos/{user_id}/{repo_name}/commits"
            commits_response = requests.get(commits_url)

            if commits_response.status_code == 200:
                commits_data = commits_response.json()
                commit_count = len(commits_data)
            else:
                commit_count = 0

            repo_commit_info.append((repo_name, commit_count))

        return repo_commit_info

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


if __name__ == "__main__":
    user = input("Enter a GitHub user ID: ").strip()
    results = get_user_repos_and_commits(user)
    if results:
        for repo, commits in results:
            print(f"Repo: {repo} Number of commits: {commits}")
    else:
        print("No repositories found or unable to fetch data.")
