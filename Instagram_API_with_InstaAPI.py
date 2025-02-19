#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://subzeroid.github.io/instagrapi/usage-guide/hashtag.html

#https://oxylabs.io/?utm_source=1430&utm_medium=affiliate&groupid=1430&transaction_id=1028580e4704eef6a6e748edfc0a8c
#https://api.hikerapi.com/docs
#https://hikerapi.com/p/bkXQlaVe
#https://github.com/subzeroid/instagrapi/tree/master
#https://subzeroid.github.io/instagrapi/usage-guide/media.html

#https://github.com/subzeroid/instagrapi/tree/master

from instagrapi import Client
import json
cl = Client()
print('asdasd')
# cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
ACCOUNT_USERNAME='sirpostchirr@gmail.com'
ACCOUNT_PASSWORD='rezvanrr2001'
SESSION_FILE = "session.json"

# cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

#
# #-- save session into file  (OK)
# session_data = cl.get_settings()
# with open(SESSION_FILE, "w") as f:
#     json.dump(session_data, f)
#
# print("Session saved!")
# #----


#--- load session from file

SESSION_FILE = "session.json"

cl = Client()

try:
    # Load session if available
    with open(SESSION_FILE, "r") as f:
        session_data = json.load(f)
        cl.set_settings(session_data)

    # Test if session is still valid
    cl.get_timeline_feed()
    print("Session restored!")

except Exception:
    # If session fails, do a fresh login
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    # Save new session
    with open(SESSION_FILE, "w") as f:
        json.dump(cl.get_settings(), f)
    print("New session saved!")



user_id = cl.user_id_from_username('kdreemz')
medias = cl.user_medias(user_id, 20)


#--- Phase1 : Get post with HASHTAG----
hashtag_name='دختر'
hashtag = cl.hashtag_info(hashtag_name)
medias = cl.hashtag_medias_top(hashtag_name, amount=20)


#---- Phase 2: Get media image, caption , comments
# Print media URLs
for m in medias:
    print(f"Media ID: {m.id}")
    print(f"Caption: {m.caption_text}")
    print(f"URL: {m.thumbnail_url}")  # For images/thumbnails of videos
    print("----")

#-- Get Cooments
# Fetch all comments
comments = cl.media_comments(medias[2].id)

# Print comments
for comment in comments:
    print(f"{comment.user.username}: {comment.text}")

#------- Get likers
# Get list of users who liked the post
likers = cl.media_likers(media_id=medias[2].id)

# Extract user IDs
user_ids = [user.pk for user in likers]

# Print user IDs
print(user_ids)

# Get media info
media_info = cl.media_info(medias[2].id)

# Get the like count
like_count = media_info.like_count

print(f"Like count: {like_count}")


#----- Check trending =====

# Function to check if a post is trending
def is_post_trending(media_id, threshold_likes=100, threshold_comments=20):
    media = cl.media_info(media_id)
    # Get the number of likes and comments
    media_info = cl.media_info(medias[2].id)
    comments = cl.media_comments(medias[2].id)

    likes = media_info.like_count
    comments = len(comments)

    # Check if the post meets the engagement thresholds
    if likes >= threshold_likes and comments >= threshold_comments:
        return True
    return False


# Example usage
trending = is_post_trending(medias[2].id)

if trending:
    print("The post is trending!")
else:
    print("The post is not trending.")


#----- Find Some posts (with Explore)
# 1. Search by Location
# 2. Search by User
# 3. Explore Feed
# 4. Get Posts from a Specific Hashtag
# 5. Get Posts from Your Feed


# Function to get explore feed
def get_explore_feed(count=10):
    explore_items = cl.explore_page()
    return explore_items

# Example usage
posts = get_explore_feed()

for post in posts:
    print(f"Post ID: {post.id}, Likes: {post.likes}, Caption: {post.caption_text}")
