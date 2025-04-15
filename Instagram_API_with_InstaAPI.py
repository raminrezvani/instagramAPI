#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://github.com/subzeroid/instagrapi/tree/master/docker
#https://subzeroid.github.io/instagrapi/usage-guide/hashtag.html
from dataclasses import replace
from pathlib import Path
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
# ACCOUNT_USERNAME='sirpostchirr@gmail.com'
# ACCOUNT_PASSWORD='rezvanrr2001'


ACCOUNT_USERNAME='0101test0101'
ACCOUNT_PASSWORD='em2n2ic27dH9mNA'
SESSION_FILE = "session_0101test0101.json"

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

class CrawlInstagram:
    def __init__(self):
        # Constants
        self.VIDEO_DOWNLOAD_DIR = 'InstagramVideoDownloaded'
        self.IMAGE_DOWNLOAD_DIR = 'InstagramImageDownloaded'
        self.DB_CONNECTION = 'mongodb://45.149.76.168:13667'
        self.DB_NAME = 'Mohaddes_Project'
        
        # Initialize directories
        self._init_directories()

        # Initialize connections
        self.cl = self._init_instagram_client()
        self.db_client = self._init_database()
        
        # Initialize thread pools
        self.media_executor = ThreadPoolExecutor(max_workers=100)
        self.ai_executor = ThreadPoolExecutor(max_workers=1)
        
        # State tracking
        self.processed_videos = set()  # Using set for O(1) lookup
        self.media_futures = []
        self.ai_futures = []
        self.media_counter = 1
        
        # Fix: Initialize lst_videos and itter
        self.lst_videos = []
        self.itter = 1

        self.future_ai = []
        self.myclient2 = pymongo.MongoClient('mongodb://45.149.76.168:13667')
        self.mydb2 = self.myclient2["Mohaddes_Project"]
        self.executorAI = ThreadPoolExecutor(max_workers=1)
    def _init_directories(self):
        """Initialize required directories"""
        os.makedirs(self.VIDEO_DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(self.IMAGE_DOWNLOAD_DIR, exist_ok=True)

    def _init_database(self):
        """Initialize MongoDB connection and collections"""
        client = pymongo.MongoClient(self.DB_CONNECTION)
        db = client[self.DB_NAME]
        self.posts_collection = db["Post_INFO_1404"]
        self.ai_results_collection = db["AI_Analysis_Results"]
        return client

    def _init_instagram_client(self):
        """Initialize Instagram client with session handling"""
        cl = Client()
        try:
            with open(SESSION_FILE, "r") as f:
                cl.set_settings(json.load(f))
            cl.get_timeline_feed()  # Test session
            print("Session restored successfully")
        except Exception:
            cl = Client()
            cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
            with open(SESSION_FILE, "w") as f:
                json.dump(cl.get_settings(), f)
            print("New session created")
        return cl

    def download_media(self, url, media_type, media_id):
        """Media download handler"""
        try:
            response = requests.get(url)
            download_dir = self.VIDEO_DOWNLOAD_DIR if media_type == 'video' else self.IMAGE_DOWNLOAD_DIR
            extension = '.mp4' if media_type == 'video' else '.jpg'
            
            file_path = os.path.join(download_dir, f"{media_type}_{media_id}{extension}")
            with open(file_path, "wb") as f:
                f.write(response.content)
            
            print(f'{file_path} downloaded successfully')
            return file_path
        except Exception as e:
            print(f"Error downloading {media_type}: {str(e)}")
            return None


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
        while True:
            try:
                time.sleep(3)
                explore_items = self.cl.explore_page()

                lst = explore_items['sectional_items']
                for item in lst:
                    try:
                        if 'fill_items' in item['layout_content']:
                            lst_1 = item['layout_content']['fill_items']
                        if 'medias' in item['layout_content']:
                            lst_1 = item['layout_content']['medias']

                        for item1 in lst_1:
                            try:
                                # Prepare post data for MongoDB
                                post_data = {
                                    "id": item1['media'].get('id', ''),
                                    "pk": item1['media'].get('pk', ''),
                                    "taken_at": item1['media'].get('taken_at', ''),
                                    "media_type": item1['media'].get('media_type', ''),
                                    "code": item1['media'].get('code', ''),
                                    "caption_text": item1['media'].get('caption', {}).get('text', ''),
                                    "user_fullname": item1['media'].get('user', {}).get('full_name', ''),
                                    "user_username": item1['media'].get('user', {}).get('username', ''),
                                    "user_pk": item1['media'].get('user', {}).get('pk', ''),
                                    "like_count": item1['media'].get('like_count', 0),
                                    "comment_count": item1['media'].get('comment_count', 0),
                                    "view_count": item1['media'].get('view_count', 0),
                                    "play_count": item1['media'].get('play_count', 0),
                                    "source": "explore",
                                    "created_at": datetime.now(),
                                    "thumbnail_url": item1['media']['image_versions2']['candidates'][0]['url'] if 'image_versions2' in item1['media'] else '',
                                    "video_urls": [vid['url'] for vid in item1['media'].get('video_versions', [])]
                                }

                                # Save to MongoDB
                                # Save to MongoDB - Update existing fields and add new ones
                                update_fields = {
                                    "like_count": post_data["like_count"],
                                    "comment_count": post_data["comment_count"],
                                    "view_count": post_data["view_count"],
                                    "play_count": post_data["play_count"],
                                    "last_updated": datetime.now()
                                }
                                
                                self.posts_collection.update_one(
                                    {"id": post_data["id"]},
                                    {
                                        "$set": update_fields,
                                        "$setOnInsert": {k: v for k, v in post_data.items() if k not in update_fields}
                                    },
                                    upsert=True
                                )

                                # Download media files
                                if 'image_versions2' in item1['media']:
                                    item_url = item1['media']['image_versions2']['candidates'][0]['url']
                                    print(f'image === {item_url}')
                                    self.media_futures.append(
                                        self.media_executor.submit(
                                            self.download_media,
                                            item_url,
                                            'image',
                                            post_data['id']
                                        )
                                    )
                                
                                if 'video_versions' in item1['media']:
                                    for vid in item1['media']['video_versions']:
                                        videoURL = vid['url']
                                        if videoURL not in self.lst_videos:
                                            print(f'video _{self.itter} ==== {videoURL} ')
                                            self.media_futures.append(
                                                self.media_executor.submit(
                                                    self.download_media,
                                                    videoURL,
                                                    'video',
                                                    str(self.itter)
                                                )
                                            )
                                            self.itter += 1
                                            self.lst_videos.append(videoURL)

                            except Exception as e:
                                print(f"Error processing media item: {str(e)}")
                                continue

                    except Exception as e:
                        print(f"Error processing section item: {str(e)}")
                        continue
                        
                print('Explore page processed')
                
            except Exception as e:
                print(f"Error fetching explore page: {str(e)}")
                time.sleep(5)  # Wait longer on error





    # --- Phase1 : Get post with HASHTAG----
    def get_hashtags(self):
        """Fetch and process posts from hashtags"""
        try:
            # Read hashtags from file with error handling
            with open('lst_hashtags.txt', 'r', encoding='utf-8') as f:
                hashtags = [tag.strip() for tag in f.readlines() if tag.strip()]

            for hashtag_name in hashtags:
                try:
                    # Get hashtag info and top media
                    hashtag_info = self.cl.hashtag_info(hashtag_name)
                    medias = self.cl.hashtag_medias_top(hashtag_name, amount=10)

                    for media in medias:
                        # Process each media item
                        media_data = self._prepare_media_data(media, hashtag_name)
                        
                        # Download media files
                        if media_data['video_url']:
                            self.media_futures.append(
                                self.media_executor.submit(
                                    self.download_media,
                                    media_data['video_url'],
                                    'video',
                                    media_data['id']
                                )
                            )

                        if media_data['thumbnail_url']:
                            self.media_futures.append(
                                self.media_executor.submit(
                                    self.download_media,
                                    media_data['thumbnail_url'],
                                    'image',
                                    media_data['id']
                                )
                            )

                        # Save to database if not exists
                        self.posts_collection.update_one(
                            {"id": media_data["id"]},
                            {"$setOnInsert": media_data},
                            upsert=True
                        )

                except Exception as e:
                    print(f"Error processing hashtag {hashtag_name}: {str(e)}")
                    continue

        except Exception as e:
            print(f"Error in get_hashtags: {str(e)}")

    def _prepare_media_data(self, media, hashtag_name):
        """Prepare media data dictionary"""
        caption_text = str(media.caption_text or '')
        
        # Clean caption text
        clean_caption = (caption_text.replace('\n', ' ')
                        .replace('.', ' ')
                        .replace('➖', ',')
                        .replace('$', '&')
                        .replace('-', '')
                        .replace('#', ' ')
                        .replace('@', ' ')
                        .replace(',', '')
                        .replace('_', ' ')
                        .strip())
        
        clean_caption = remove_emojis(clean_caption)
        clean_caption = remove_special_chars(clean_caption)

        return {
            'caption_text': clean_caption.encode('utf8').decode('utf8'),
            'hashtag': hashtag_name,
            'code': media.code,
            'comment_count': media.comment_count,
            'id': media.id,
            'like_count': media.like_count,
            'location': '',
            'media_type': media.media_type,
            'pk': media.pk,
            'play_count': media.play_count,
            'product_type': media.product_type,
            'taken_at': media.taken_at,
            'thumbnail_url': str(media.thumbnail_url) if media.thumbnail_url else '',
            'user_fullname': media.user.full_name,
            'user_isPrivate': media.user.is_private,
            'user_pk': media.user.pk,
            'user_profilePic': str(media.user.profile_pic_url),
            'user_username': media.user.username,
            'usertags': str(media.usertags),
            'video_url': str(media.video_url) if media.video_url else '',
            'view_count': str(media.view_count) if media.view_count else '',
            'created_at': datetime.now()
        }

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

    def Batch_ai(self):

        directory = "InstagramVideoDownloaded"

        # Create new collection for AI results
        self.mycol_ai_results = self.mydb2["AI_Analysis_Results"]

        path = Path(directory)
        files = [file.name for file in path.iterdir() if file.is_file()]

        for file in files:
            file_path = os.path.join(directory, file)
            self.future_ai.append(self.executorAI.submit(self.google_ai_perform_and_save, file_path, file))

        print('Processing started...')

        t1 = datetime.now()
        for fu in self.future_ai:
            try:
                fu.result()
            except Exception as e:
                print(f'a task failed with error {e}')
        t2 = datetime.now()
        spendtime = (t2 - t1).total_seconds()
        print(f'SpendTime =={spendtime}')
        print('finish')

    def process_media_with_ai(self, media_type='video'):
        """Process all media files with Google AI"""
        directory = "InstagramVideoDownloaded" if media_type == 'video' else "InstagramImageDownloaded"
        processor = self.google_ai_perform_and_save if media_type == 'video' else self.google_ai_perform_image
        
        try:
            # Get all media files
            files = list(Path(directory).glob('*.*'))
            if not files:
                print(f"No files found in {directory}")
                return

            print(f"Processing {len(files)} {media_type} files...")
            start_time = datetime.now()

            # Process files in parallel
            futures = []
            for file_path in files:
                futures.append(
                    self.executorAI.submit(
                        processor,
                        str(file_path),
                        file_path.name
                    )
                )

            # Wait for all tasks to complete
            for future in futures:
                try:
                    future.result(timeout=300)  # 5 minutes timeout per file
                except Exception as e:
                    print(f"Task failed: {str(e)}")

            elapsed_time = (datetime.now() - start_time).total_seconds()
            print(f"Processing completed in {elapsed_time:.2f} seconds")

        except Exception as e:
            print(f"Error in batch processing: {str(e)}")

    def google_ai_perform_and_save(self, video_path, videoID):
        """Process video with Google AI and save results"""
        try:
            # Initialize AI client and process video
            client_ai = googleAI()
            client_ai.UploadVideo(video_path)
            ai_response = client_ai.GetAI()

            if not ai_response:
                print(f"No AI response for video {videoID}")
                return

            # Extract topics safely
            topics_dict = ai_response.get("Topics", {})
            
            # Prepare AI analysis result
            ai_result = {
                "video_id": videoID,
                "video_path": video_path,
                "analysis_date": datetime.now(),
                "raw_ai_response": ai_response,
                "content_type": ["Video"],
                "topics": list(topics_dict.keys()),
                "emotions": ai_response.get("Subcategory of Feels and Emotion", []),
                "languages": ai_response.get("Language", []),
                "sensitivity": ai_response.get("Sensitivity", []),
                "gender": ai_response.get("Gender", []),
                "audience": ai_response.get("Audience", []),
                "age_range": ai_response.get("Age Range", []),
                "true_explore_mode": "Enabled",
                "credibility": ["Regular Poster"],
                "social_activities": [],
                "content_verification": ai_response.get("Content Verification", []),
                "source": ["User Generated"],
                "post_time": ["Today"],
                "sentiment": ["Neutral"],
                "lifestyles_personal": list(topics_dict.get("Lifestyle & Personal", {}).keys()),
                "trends": ["Stable"]
            }

            # Save to MongoDB
            self.ai_results_collection.update_one(
                {"video_id": videoID},
                {"$set": ai_result},
                upsert=True
            )

            # Organize files in categorized folders
            self._organize_media_files(ai_response, video_path, videoID, 'video')
            
            return True

        except Exception as e:
            print(f"Error processing video {videoID}: {str(e)}")
            return False

    def google_ai_perform_image(self, image_path, imageID):
        """Process image with Google AI and save results"""
        try:
            # Initialize AI client and process image
            client_ai = googleAI()
            ai_response = client_ai.GetAI_Image(image_path)
            
            if not ai_response:
                print(f"No AI response for image {imageID}")
                return

            # Extract topics
            topics = ai_response.get('topics', ai_response.get('Topics', {}))
            
            # Save results and organize files
            self._organize_media_files(topics, image_path, imageID, 'image')
            
            return True

        except Exception as e:
            print(f"Error processing image {imageID}: {str(e)}")
            return False

    def _organize_media_files(self, ai_response, source_path, media_id, media_type):
        """Organize media files based on AI analysis"""
        try:
            # Get main category and subcategory
            main_category = list(ai_response.keys())[0]
            sub_category = list(ai_response[main_category].keys())[0]

            # Create folder structure
            category_path = os.path.join(main_category, sub_category)
            os.makedirs(category_path, exist_ok=True)

            # Determine file extension
            extension = '.mp4' if media_type == 'video' else '.jpg'
            
            # Copy file to categorized folder
            dest_path = os.path.join(category_path, f"{media_type}_{media_id}{extension}")
            shutil.copy2(source_path, dest_path)  # copy2 preserves metadata

            # Optional: Save AI response as JSON
            json_path = dest_path.replace(extension, '.json')
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(ai_response, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"Error organizing {media_type} {media_id}: {str(e)}")

    def google_ai_perform(self, video_path, videoID):
        # ---
        try:
            clientAI = googleAI()
            clientAI.UploadVideo(video_path)
            parsed_json = clientAI.GetAI()
            base_parsed_json = parsed_json
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
            # jsonPath=destination_file_path.replace('.mp4','.json')
            # fileName=destination_file_path.split('\\')[-1].replace('.mp4','')+'.json'
            # jsonPath=os.path.join(destination_file_path.split('\\')[0:-1],fileName)
            # with open(jsonPath,'w') as f:
            #     f.write(str(json.dumps(base_parsed_json)))

        except Exception as e:
            print(str(e))
            return ''


#-- initialize
obj_insta=CrawlInstagram()


#=========================
# get Explore
obj_insta.get_explore_posts()


# AI for Video
# For videos
# obj_insta.process_media_with_ai('video')

# For images
# obj_insta.process_media_with_ai('image')



#AI for Image
# obj_insta.Batch_ai_Image()
#=========================





#--- Other ----
# obj_insta.get_hashtags()
# hashtag='بدنسازی'
# obj_insta.get_Comments(hashtag)
# obj_insta.get_images(hashtag)
# obj_insta.get_feeds()





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