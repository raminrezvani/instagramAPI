#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://subzeroid.github.io/instagrapi/usage-guide/hashtag.html
from dataclasses import replace

#https://oxylabs.io/?utm_source=1430&utm_medium=affiliate&groupid=1430&transaction_id=1028580e4704eef6a6e748edfc0a8c
#https://api.hikerapi.com/docs
#https://hikerapi.com/p/bkXQlaVe
#https://github.com/subzeroid/instagrapi/tree/master
#https://subzeroid.github.io/instagrapi/usage-guide/media.html

#https://github.com/subzeroid/instagrapi/tree/master

from instagrapi import Client
import json
# cl = Client()
# print('asdasd')
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

import emoji

def remove_emojis(text):
    return emoji.replace_emoji(text, replace='')  # Removes all emojis
import re

def remove_special_chars(text):
    return re.sub(r"[^\w\s]", "", text)  # Removes all non-word and non-space characters
#--- load session from file

SESSION_FILE = "session.json"

import pymongo
class CrawlInstagram():
    def __init__(self):
        self.cl=self.load_account()
        self.myclient2 = pymongo.MongoClient('mongodb://45.149.76.168:13667')
        self.mydb2 = self.myclient2["Mohaddes_Project"]
        self.mycol_write_posts = self.mydb2["Post_Hashtags"]

    def load_account(self):
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
        return cl

    # --- Phase1 : Get post with HASHTAG----
    def get_hashtags(self):
        with open('lst_hashtags.txt','r',encoding='utf-8') as f:
            hastags=[a.replace('\n','') for a in f.readlines()]

        for hashtag_name in hastags:
            hashtag_sample = self.cl.hashtag_info(hashtag_name)
            medias = self.cl.hashtag_medias_top(hashtag_name, amount=1000)
            for media in medias:
                one_sample={}
                one_sample['caption_text']=((str(media.caption_text)
                                            .replace('\n',' ')
                                            .replace('.',' ')).replace('➖', ',')
                                            .replace('$','&').replace('-','')
                                            .replace('#',' ').replace('@',' ')
                                            .replace(',','').replace('_',' ')).strip().encode('utf8').decode('utf8')

                one_sample["caption_text"] = remove_emojis(one_sample["caption_text"]).encode('utf8').decode('utf8')
                one_sample["caption_text"] = remove_special_chars(one_sample["caption_text"]).encode('utf8').decode('utf8')

                one_sample['code'] = media.code
                one_sample['comment_count'] = media.comment_count
                one_sample['id'] = media.id
                one_sample['like_count'] = media.like_count
                # one_sample['location'] = media.location
                one_sample['location'] = ''
                one_sample['media_type'] = media.media_type
                one_sample['pk'] = media.pk
                one_sample['play_count'] = media.play_count
                one_sample['product_type'] = media.product_type
                one_sample['taken_at'] = media.taken_at
                one_sample['thumbnail_url'] = str(media.thumbnail_url)
                one_sample['user_fullname'] = media.user.full_name
                one_sample['user_isPrivate'] = media.user.is_private
                one_sample['user_pk'] = media.user.pk
                one_sample['user_profilePic'] =str(media.user.profile_pic_url)
                one_sample['user_username'] = media.user.username
                one_sample['usertags'] = str(media.usertags)

                one_sample['video_url'] = str(media.video_url) if media.video_url is not None else ''
                one_sample['view_count'] = str(media.view_count) if media.view_count is not None else ''

                # Check if the ID exists and insert only if it does not exist
                existing_doc = self.mycol_write_posts.find_one({"id": one_sample["id"]})
                if not existing_doc:
                    self.mycol_write_posts.insert_one(one_sample)

            print(medias)

    def get_Comments(self):

        lst_medias = self.mycol_write_posts.find({'comments':{'$exists':False}})
        # # get comments
        for media in lst_medias:
            try:
                # media_info = self.cl.media_info(media['id'])
                comments = self.cl.media_comments(media['id'])
                comments_txt=[a.text for a in comments]
                update = {"$set": {"comments": comments_txt}}  # Change 'field_name' and 'new_value'
                self.mycol_write_posts.update_one({'id':media['id']}, update)
            except Exception as e:
                print(str(e))
                continue

    def get_images(self):
        import requests
        import os
        folder_name='ImageDownloaded'
        os.makedirs(folder_name,exist_ok=True)
        lst_medias = self.mycol_write_posts.find({'downloadIMG': {'$exists': False}})
        # # get comments
        for media in lst_medias:
            try:
                imageURL=media['thumbnail_url']
                imageID=media['id']
                fileName = os.path.join(folder_name, imageID)

                # Send a GET request
                response = requests.get(imageURL, stream=True)

                # Check if the request was successful
                if response.status_code == 200:
                    with open(f'{fileName}.jpg', "wb") as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    print("Image downloaded successfully.")
                else:
                    print(f"Failed to download image. Status code: {response.status_code}")

                update = {"$set": {"downloadIMG": 1}}  # Change 'field_name' and 'new_value'
                self.mycol_write_posts.update_one({'id': media['id']}, update)
            except Exception as e:
                print(str(e))
                continue


#-- calling
obj_insta=CrawlInstagram()
# obj_insta.get_hashtags()
# obj_insta.get_Comments()
obj_insta.get_images()






# user_id = cl.user_id_from_username('kdreemz')
# medias = cl.user_medias(user_id, 20)





#---- Phase 2: Get media image, caption , comments
# Print media URLs
# for m in medias:
#     print(f"Media ID: {m.id}")
#     print(f"Caption: {m.caption_text}")
#     print(f"URL: {m.thumbnail_url}")  # For images/thumbnails of videos
#     print("----")

# #-- Get Cooments
# # Fetch all comments
# comments = cl.media_comments(medias[2].id)
#
# # Print comments
# for comment in comments:
#     print(f"{comment.user.username}: {comment.text}")
#
# #------- Get likers
# # Get list of users who liked the post
# likers = cl.media_likers(media_id=medias[2].id)
#
# # Extract user IDs
# user_ids = [user.pk for user in likers]
#
# # Print user IDs
# print(user_ids)
#
# # Get media info
# media_info = cl.media_info(medias[2].id)
#
# # Get the like count
# like_count = media_info.like_count
#
# print(f"Like count: {like_count}")
#
#
# #----- Check trending =====
#
# # Function to check if a post is trending
# def is_post_trending(media_id, threshold_likes=100, threshold_comments=20):
#     media = cl.media_info(media_id)
#     # Get the number of likes and comments
#     media_info = cl.media_info(medias[2].id)
#     comments = cl.media_comments(medias[2].id)
#
#     likes = media_info.like_count
#     comments = len(comments)
#
#     # Check if the post meets the engagement thresholds
#     if likes >= threshold_likes and comments >= threshold_comments:
#         return True
#     return False
#
#
# # Example usage
# trending = is_post_trending(medias[2].id)
#
# if trending:
#     print("The post is trending!")
# else:
#     print("The post is not trending.")
#

#----- Find Some posts (with Explore)
# 1. Search by Location
# 2. Search by User
# 3. Explore Feed
# 4. Get Posts from a Specific Hashtag
# 5. Get Posts from Your Feed

#
# # Function to get explore feed
# def get_explore_feed(count=10):
#     explore_items = cl.explore_page()
#     return explore_items
#
# # Example usage
# posts = get_explore_feed()
#
# for post in posts:
#     print(f"Post ID: {post.id}, Likes: {post.likes}, Caption: {post.caption_text}")
