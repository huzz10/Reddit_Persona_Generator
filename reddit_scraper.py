import requests
import time

def get_user_posts(username, limit=30):
    url = f"https://www.reddit.com/user/{username}/submitted.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    posts = []
    if res.status_code == 200:
        data = res.json().get("data", {}).get("children", [])
        for item in data[:limit]:
            post = item["data"]
            posts.append({
                "title": post.get("title", ""),
                "body": post.get("selftext", ""),
                "url": f"https://www.reddit.com{post.get('permalink', '')}"
            })
    else:
        print(f"Failed to fetch posts: {res.status_code}")
    time.sleep(1)
    return posts

def get_user_comments(username, limit=30):
    url = f"https://www.reddit.com/user/{username}/comments.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    comments = []
    if res.status_code == 200:
        data = res.json().get("data", {}).get("children", [])
        for item in data[:limit]:
            comment = item["data"]
            comments.append({
                "body": comment.get("body", ""),
                "link": f"https://www.reddit.com{comment.get('permalink', '')}"
            })
    else:
        print(f"Failed to fetch comments: {res.status_code}")
    time.sleep(1)
    return comments

def get_user_data(username, limit=30):
    posts = get_user_posts(username, limit)
    comments = get_user_comments(username, limit)
    return posts, comments

