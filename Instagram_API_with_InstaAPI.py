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


#
# #--- Instal loader example
# from instaloader import Instaloader, Profile
#
# loader = Instaloader()
#
# # Log in as the other user
# loader.login("sirpostchirr@gmail.com", "rezvanrr2001")  # Replace with their credentials
#
# # Get their profile
# profile = Profile.from_username(loader.context, loader.context.username)
#
# # Fetch their timeline feed
# for post in profile.get_feed_posts():
#     print(f"Post URL: {post.url}")
#     print(f"Caption: {post.caption or 'No caption'}")
#     print(f"Owner: {post.owner_username}")
#     print(f"Date: {post.date}")
#     print("---")

#----------

#--- User passwords
# 0101test0101
# em2n2ic27dH9mNA

# 0202test0202
# EGM7PrJjY3UWRp6

# parsalbahar307@gmail.com.
# 0303test0303
# XZASyz4bJnRn4g4
# cl.login('0303test0303','XZASyz4bJnRn4g4')
#---------------

#_--------
import time
from os.path import exists
import shutil
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
from datetime import datetime
import emoji
import requests
import os
from google_ai import googleAI
os.makedirs('InstagramVideoDownloaded',exist_ok=True)
os.makedirs('InstagramImageDownloaded',exist_ok=True)

def remove_emojis(text):
    return emoji.replace_emoji(text, replace='')  # Removes all emojis
import re

def remove_special_chars(text):
    return re.sub(r"[^\w\s]", "", text)  # Removes all non-word and non-space characters
#--- load session from file

SESSION_FILE_khodam = "session.json"
SESSION_FILE_0101test0101 = "session_0101test0101.json"
SESSION_FILE_0202test0202 = "session_0202test0202.json"


#
# SESSION_FILE = "session.json"
SESSION_FILE = "session_0101test0101.json"
# SESSION_FILE = "session_0202test0202.json"
# SESSION_FILE = "session_0303test0303.json"
import pymongo
from concurrent.futures import ThreadPoolExecutor

class CrawlInstagram():
    def __init__(self):
        self.cl=self.load_account()
        self.myclient2 = pymongo.MongoClient('mongodb://45.149.76.168:13667')
        self.mydb2 = self.myclient2["Mohaddes_Project"]
        self.mycol_write_posts = self.mydb2["Post_Hashtags"]

        self.timeline_feed=''
        self.executor=ThreadPoolExecutor(max_workers=100)
        self.executorAI=ThreadPoolExecutor(max_workers=1)
        self.future=[]
        self.future_ai = []
        self.itter=1
        self.lst_videos=[]
    def downloadVideo(self,videoURL,videoID):
        response = requests.get(videoURL)
        with open(f"InstagramVideoDownloaded/video_{videoID}.mp4", "wb") as f:
            f.write(response.content)
        print(f'InstagramVideoDownloaded/video _ {videoID}___ is downloaded successfully.')

    def Batch_ai(self):
        from pathlib import Path
        directory = "InstagramVideoDownloaded"

        path = Path(directory)
        files=[file.name for file in path.iterdir() if file.is_file()]

        for file in files:
            file_path=os.path.join(directory,file)
            self.future_ai.append(self.executorAI.submit(self.google_ai_perform,file_path,file))
            # self.google_ai_perform( file_path,file)
        print('pass')

        t1=datetime.now()
        for fu in self.future_ai:
            try:
                fu.result()
            except Exception as e:
                print(f'a task is failed with error {e}')
        t2=datetime.now()
        spendtime=(t2-t1).total_seconds()
        print(f'SpendTime =={spendtime}')
        print('finish')

    #asdasd

    def Batch_ai_Image(self):

        from pathlib import Path
        directory = "InstagramImageDownloaded"

        path = Path(directory)
        files=[file.name for file in path.iterdir() if file.is_file()]

        for file in files:
            file_path=os.path.join(directory,file)
            self.future_ai.append(self.executorAI.submit(self.google_ai_perform_image,file_path,file))
            # self.google_ai_perform( file_path,file)
        print('pass')

        t1=datetime.now()
        for fu in self.future_ai:
            try:
                fu.result()
            except Exception as e:
                print(f'a task is failed with error {e}')
        t2=datetime.now()
        spendtime=(t2-t1).total_seconds()
        print(f'SpendTime =={spendtime}')
        print('finish')



    def google_ai_perform_image(self,image_path,imageID):
        try:
            clientAI = googleAI()
            parsed_json = clientAI.GetAI_Image(image_path)
            base_parsed_json = parsed_json
            try:
                parsed_json = parsed_json['topics']
            except:
                ''
            try:
                parsed_json = parsed_json['Topics']
            except:
                ''
            # ---- insert into folder
            # Get the main folder name (the top-level key)
            try:
                main_folder = list(parsed_json.keys())[0]  # "Travel, Adventure & Nature"
            except:
                return ''

            # Get the subfolder name (the nested key)
            sub_folder = list(parsed_json[main_folder].keys())[0]  # "City Guides"

            # Create the main folder
            os.makedirs(main_folder, exist_ok=True)

            # Create the subfolder inside the main folder
            subfolder_path = os.path.join(main_folder, sub_folder)
            os.makedirs(subfolder_path, exist_ok=True)

            destination_file_path = os.path.join(subfolder_path, f"image_{imageID}.jpg")
            # Copy the file
            shutil.copy(image_path, destination_file_path)

            # Create Json file
            jsonPath = destination_file_path.replace('.jpg', '.json')
            with open(jsonPath, 'w') as f:
                f.write(str(json.dumps(base_parsed_json)))

        except Exception as e:
            print(str(e))
            return ''
        pass

    def google_ai_perform(self,video_path,videoID):
        # ---
        try:
            clientAI = googleAI()
            clientAI.UploadVideo(video_path)
            parsed_json = clientAI.GetAI()
            base_parsed_json=parsed_json
            # t2 = datetime.now()
            # spendTime = (t2 - t1).total_seconds()
            # print(f'Timespend ==== {spendTime}')
            try:
                parsed_json = parsed_json['topics']
            except:
                ''
            try:
                parsed_json = parsed_json['Topics']
            except:
                ''
            # ---- insert into folder
            # Get the main folder name (the top-level key)
            try:
                main_folder = list(parsed_json.keys())[0]  # "Travel, Adventure & Nature"
            except:
                return ''

            # Get the subfolder name (the nested key)
            sub_folder = list(parsed_json[main_folder].keys())[0]  # "City Guides"

            # Create the main folder
            os.makedirs(main_folder, exist_ok=True)

            # Create the subfolder inside the main folder
            subfolder_path = os.path.join(main_folder, sub_folder)
            os.makedirs(subfolder_path, exist_ok=True)

            destination_file_path = os.path.join(subfolder_path, f"video_{videoID}.mp4")
            # Copy the file
            shutil.copy(video_path, destination_file_path)

            # Create Json file
            jsonPath=destination_file_path.replace('.mp4','.json')
            # fileName=destination_file_path.split('\\')[-1].replace('.mp4','')+'.json'
            # jsonPath=os.path.join(destination_file_path.split('\\')[0:-1],fileName)
            with open(jsonPath,'w') as f:
                f.write(str(json.dumps(base_parsed_json)))

        except Exception as e:
            print(str(e))
            return ''


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
            cl = Client()
            # If session fails, do a fresh login
            cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
            # Save new session
            with open(SESSION_FILE, "w") as f:
                json.dump(cl.get_settings(), f)
            print("New session saved!")
        return cl

    def get_explore_posts(self):
        while(True):
            try:
                time.sleep(3)
                explore_items=self.cl.explore_page()

                lst=explore_items['sectional_items']
                for item in lst:
                    try:
                        if ('fill_items' in item['layout_content']):
                            lst_1=item['layout_content']['fill_items']
                        if ('medias' in item['layout_content']):
                            lst_1 = item['layout_content']['medias']

                        for item1 in lst_1:
                            try:
                                item_url=item1['media']['image_versions2']['candidates'][0]['url']
                                print(f'image === {item_url}')
                            except:
                                ''
                            try:
                                lst_video = item1['media']['video_versions']
                                for vid in lst_video:
                                    videoURL=vid['url']
                                    if (videoURL not in self.lst_videos):
                                        print(f'video _{self.itter} ==== {videoURL} ')
                                        self.future.append(self.executor.submit(self.downloadVideo,videoURL,str(self.itter)))
                                        self.itter=self.itter+1

                                        self.lst_videos.append(videoURL)
                            except Exception as e:
                                print(str(e))
                                ''


                    except:
                        continue
                print('zssd')
            except Exception as e:
                print(str(e))





    # --- Phase1 : Get post with HASHTAG----
    def get_hashtags(self):
        with open('lst_hashtags.txt','r',encoding='utf-8') as f:
            hastags=[a.replace('\n','') for a in f.readlines()]

        for hashtag_name in hastags:
            hashtag_sample = self.cl.hashtag_info(hashtag_name)
            medias = self.cl.hashtag_medias_top(hashtag_name, amount=10)
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

                one_sample['hashtag'] = hashtag_name
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
                one_sample['thumbnail_url'] = str(media.thumbnail_url) if media.thumbnail_url is not None else ''
                one_sample['user_fullname'] = media.user.full_name
                one_sample['user_isPrivate'] = media.user.is_private
                one_sample['user_pk'] = media.user.pk
                one_sample['user_profilePic'] =str(media.user.profile_pic_url)
                one_sample['user_username'] = media.user.username
                one_sample['usertags'] = str(media.usertags)

                one_sample['video_url'] = str(media.video_url) if media.video_url is not None else ''
                one_sample['view_count'] = str(media.view_count) if media.view_count is not None else ''

                # ------------------
                # download image or video
                # -----------
                if (one_sample['video_url'] != ''):
                    videoURL = one_sample['video_url']
                    videoID = one_sample['id']

                    t1=datetime.now()
                    response = requests.get(videoURL)
                    with open(f"InstagramVideoDownloaded/video_{videoID}.mp4", "wb") as f:
                        f.write(response.content)
                    print(f'InstagramVideoDownloaded/video _ {videoID}___ is downloaded successfully.')






                if (one_sample['thumbnail_url'] != ''):

                    ImageURL = one_sample['thumbnail_url']
                    response = requests.get(ImageURL)
                    with open(f"InstagramImageDownloaded/Image_{one_sample['id'] }.jpg", "wb") as f:
                        f.write(response.content)
                    print(
                        f'InstagramImageDownloaded/Image_ _ {one_sample['id']}___ is downloaded successfully.')



                # Check if the ID exists and insert only if it does not exist
                existing_doc = self.mycol_write_posts.find_one({"id": one_sample["id"]})
                if not existing_doc:
                    self.mycol_write_posts.insert_one(one_sample)

            print(medias)

    def get_Comments(self,hashtag):

        lst_medias = self.mycol_write_posts.find({'hashtag':hashtag,'comments':{'$exists':False}})
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

    def get_images(self,hashtag):
        import requests
        import os
        folder_name=f'ImageDownloaded/{hashtag}'
        os.makedirs(folder_name,exist_ok=True)
        lst_medias = self.mycol_write_posts.find({'hashtag':hashtag,'downloadIMG': {'$exists': False}})
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


    def get_feeds(self):
        # adds a random delay between 1 and 3 seconds after each request
        self.cl.delay_range = [1, 3]

        # get feeds
        # timeline_feed = self.cl.get_timeline_feed()
        count=10
        parsed_feed = {}
        max_id=0

        while(True):
            # Fetch timeline feed
            try:
                if (count<=0):
                    break
                count=count-1

                if (max_id!=0):
                    self.timeline_feed = self.cl.get_timeline_feed(max_id = max_id)
                    max_id = self.timeline_feed['next_max_id']
                else:
                    self.timeline_feed = self.cl.get_timeline_feed()

                print(f"Fetched {len(self.timeline_feed)} posts from timeline feed")
                # Parse and format the results into a JSON-compatible structure
                for item in self.timeline_feed['feed_items']:

                    if 'media_or_ad' in item:
                        try:
                            item = item['media_or_ad']
                            post_data = {
                                "post_id": item['id'] if 'id' in item else '',
                                "post_pk": item['pk'] if 'pk' in item else '',
                                "taken_at": item['taken_at'] if 'taken_at' in item else '',
                                "media_type": item['media_type'] if 'media_type' in item else '',
                                "code": item['code'] if 'code' in item else '',
                                "post_caption":item['caption']['text'] if 'caption' in item else '',
                                "media_id": item['caption']['media_id'] if 'caption' in item else '',
                                "user_id": item['caption']['user_id'] if 'caption' in item else '',
                                "username": item['caption']['user']['username'] if 'caption' in item else '',
                                "full_name": item['caption']['user']['full_name'] if 'caption' in item else '',
                                "play_count": item['play_count'] if 'play_count' in item else '',
                                "image_version2":[a['url'] for a in item['image_versions2']['candidates']] if 'image_versions2' in item else '',

                                "comment_count": item['comment_count'] if 'comment_count' in item else '',
                                "video_version": [{'id':a['id'],'url':a['url']} for a in item['video_versions']] if 'video_versions' in item else '',

                            }

                            #------------------
                            # download image or video
                            #-----------
                            if (post_data['video_version']!=0):
                                for vv in post_data['video_version']:
                                    videoURL=vv['url']
                                    videoID = vv['id']

                                    response = requests.get(videoURL)
                                    with open(f"InstagramVideoDownloaded/video_{videoID}.mp4", "wb") as f:
                                        f.write(response.content)
                                    print(f'InstagramVideoDownloaded/video _ {videoID}___ is downloaded successfully.')

                            if (post_data['image_version2']!=0):
                                for img in post_data['image_version2']:
                                    ImageURL=img
                                    response = requests.get(ImageURL)
                                    with open(f"InstagramImageDownloaded/Image_{post_data['post_id']}.jpg", "wb") as f:
                                        f.write(response.content)
                                    print(f'InstagramImageDownloaded/Image_ _ {post_data['post_id']}___ is downloaded successfully.')

                            # parsed_feed.append(post_data)
                            if (post_data['post_id'] not in parsed_feed):
                                parsed_feed[post_data['post_id']]=post_data
                                print('New Post')
                            else:
                                print('Old Post')


                        except:
                            print('error in parsed Posts!')

                    if 'suggested_users' in item:


                        print('Suggested.. Skiped..')



                # Save the parsed feed to a JSON file
                with open("timeline_feed.json", "w", encoding="utf-8") as f:
                    json.dump(parsed_feed, f, ensure_ascii=False, indent=4)

                print("Timeline feed saved to timeline_feed.json")

            except Exception as e:
                print(f"Error fetching timeline feed: {e}")

            time.sleep(3)



#-- calling
obj_insta=CrawlInstagram()

#=========================
# get Explore
# obj_insta.get_explore_posts()

# AI for Video
obj_insta.Batch_ai()

#AI for Image
# obj_insta.Batch_ai_Image()
#=========================




# obj_insta.get_hashtags()
# hashtag='بدنسازی'
# obj_insta.get_Comments(hashtag)
# obj_insta.get_images(hashtag)
obj_insta.get_feeds()





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

#------------------------
# get feeds
# timeline_feed = cl.get_timeline_feed()
#----------------------------