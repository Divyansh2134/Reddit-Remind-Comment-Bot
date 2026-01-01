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

for item in reddit.inbox.stream(skip_existing=True):
    # Check if the item is a comment (mentions are comments)
    if isinstance(item, praw.models.Comment):
        
        # 1. The text of the comment where you were tagged
        mention_text = item.body
        
        # 2. The author of the mention
        author = item.author.name
        
        # 3. The Post (Submission) details
        post = item.submission
        post_title = post.title
        post_url = post.url
        current_comment_count = post.num_comments
        
        print(f"New Mention by: {author}")
        print(f"Comment Text: {mention_text}")
        print(f"In Post: {post_title}")
        print(f"Current Comments: {current_comment_count}")
        
        # Mark as read so it doesn't process again next time
        item.mark_read()