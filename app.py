import json

from github import Github

with open(".config.json", "r") as fp:
    config = json.load(fp)

token = config["token"]
hostname = config["hostname"]
username = config["user"]
author = config["author"]
repo_names = config["repos"]

g = Github(base_url=f"https://{hostname}/api/v3", login_or_token=token)
user = g.get_user(username)

print("Open PRs:")

for repo_name in repo_names:
    r = user.get_repo(repo_name)
    pulls = r.get_pulls(state="open")
    for p in pulls:
        if p.user.login == author:
            print(f"<{p.url} |{p.title}>")
