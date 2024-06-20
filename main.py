import praw
import time


def get_reddit_comments(url):
    """Fetches all comments from a given Reddit post URL.

    This function uses PRAW (Python Reddit API Wrapper) to interact with the Reddit API.
    It extracts the submission ID from the URL, retrieves the submission object, and then
    recursively extracts all comments (including replies) and stores them in a list.

    **Important:** You need to obtain your own Reddit API credentials before using this function.

    Args:
        url (str): The URL of the Reddit post.

    Returns:
        list: A list of tuples containing the comment level (depth) and the comment body.
    """

    # Replace with your own Reddit API credentials (client ID, client secret, and user agent)
    # **Do not hardcode them here!**  Store them securely in a separate file or environment variable.
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT'
    )

    # Extract submission ID from URL
    submission_id = url.split('/')[-3]

    # Get submission (post) using the ID
    submission = reddit.submission(id=submission_id)

    # Ensure all comments are loaded
    submission.comments.replace_more(limit=None)

    # List to store all comments
    comments = []

    # Function to recursively extract comments
    def extract_comments(comment, level=0):
        comments.append((level, comment.body))
        for reply in comment.replies:
            extract_comments(reply, level + 1)

    # Extract comments starting from the top-level comments
    for top_level_comment in submission.comments:
        extract_comments(top_level_comment)

    return comments


post_url = input("Enter the URL of the Reddit post: ")

# Record the start time
start_time = time.time()

# get all comments
all_comments = get_reddit_comments(post_url)

# Record the end time
end_time = time.time()

# duration
duration = end_time - start_time

print(f"Time taken to extract comments: {duration:.2f} seconds")
print(f"\nTotal number of comments: {len(all_comments)}")
# print all comments
for level, comment in all_comments:
    print(f"\n{'   ' * level}comment: {comment}")


