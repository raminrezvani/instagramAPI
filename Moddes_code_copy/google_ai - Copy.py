

from google import genai
from google.genai import types
from google import genai
from google.genai import types
from google import genai
import time
from google_prompt import prompt
import json
import pathlib
import PIL.Image


class googleAI:
    def __init__(self):
        # api_key = "AIzaSyBk8LlBibrTqhcfuLQ0tu29n-5ocTgO5ZE"
        self.api_key="AIzaSyBmSb_smXgwbye1ckY9ZIt8pAdhIdq9c1M"
        self.client = genai.Client(api_key=self.api_key)
        self.prompt=prompt
        self.video_file=''
    def UploadVideo(self,video_path):
        print("Uploading file...")
        # video_file = client.files.upload(file="c:/Snapinst.app_aa.mp4")
        video_file = self.client.files.upload(file=video_path)
        print(f"Completed upload: {video_file.uri}")
        # Check whether the file is ready to be used.
        while video_file.state.name == "PROCESSING":
            print('.', end='')
            time.sleep(1)
            video_file = self.client.files.get(name=video_file.name)

        if video_file.state.name == "FAILED":
          raise ValueError(video_file.state.name)

        self.video_file=video_file
        print('Done')

    def GetAI_Image(self,image_path_1):
        # image_path_1='Image_3577537765153946545_72131956097.jpg'

        try:
            pil_image = PIL.Image.open(image_path_1)

            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[self.prompt,
                          pil_image])

            # Remove the ```json and extra formatting to get pure JSON
            cleaned_json_string = response.text.replace("```json\n", "").rstrip("```").strip()

            # Parse the JSON string into a Python dictionary
            parsed_json = json.loads(cleaned_json_string)

            # Print the parsed JSON (as a Python dictionary)
            # print(parsed_json)
            return parsed_json
        except Exception as e:
            print(str(e))
            return ''


    def GetAI(self):
        try:
            # Pass the video file reference like any other media part.
            response = self.client.models.generate_content(
                # model="gemini-1.5-pro",
                model="gemini-2.0-flash-lite-001",
                contents=[
                    self.video_file,
                    self.prompt

                ])

            # Remove the ```json and extra formatting to get pure JSON
            cleaned_json_string = response.text.replace("```json\n", "").rstrip("```").strip()

            # Parse the JSON string into a Python dictionary
            parsed_json = json.loads(cleaned_json_string)

            # Print the parsed JSON (as a Python dictionary)
            # print(parsed_json)
            return parsed_json
        except Exception as e:
            print(' Error in GetAI')
            print(str(e))
            return ''
