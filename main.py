import praw
from dotenv import load_dotenv 
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
password = os.getenv("PASSWORD")
user_agent = os.getenv("USER_AGENT")
username = os.getenv("USERNAME")


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username,
)
print(reddit.read_only)

try:
    for submission in reddit.subreddit("developerIndia").new(limit=10):
        print(submission.title)

except Exception as e:
    print("Error:", e)