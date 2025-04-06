#https://ai.google.dev/gemini-api/docs/vision?lang=python
#https://ai.google.dev/gemini-api/docs/pricing
#https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb#scrollTo=u53CdzCFXCJP
#https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb#scrollTo=u53CdzCFXCJP




# #-------- Download Video with Link --------
# import requests
# import requests
# url='https://scontent-iad3-1.cdninstagram.com/o1/v/t16/f2/m86/AQNaqme7tpyho91hCUFVqijOFV1c0RQKxfkOQXiMY0UQt-1_hQ5VAarMsvjoLvcyxZZ0sQAjae4Y-wuzmweOif-Ivo77Yc_2JYmRrSU.mp4?efg=eyJkdXJhdGlvbl9zIjo4LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwieHB2X2Fzc2V0X2lkIjoyMTU3NzI5ODM0NzAwMDI4LCJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Adg8-dvgKlwAyiIl3c3t1e9yZbV7Go5X6-TOMkBS0CV3iJwJ9nX35IqvwdO3kcwqzls&vs=901cd81cd3b32fbc&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83MzRDRjE5NEU5MUE0MzBERDc1RDJFMkJGREM1OEE4OF92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dJZlB5UndNZXc5c1NhSU5BQU9TMUkzQkZMRnlicV9FQUFBRhUCAsgBACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJvizjIW0nNUHFQIoAkMzLBdAIap--dsi0RgSZGFzaF9iYXNlbGluZV8xX3YxEQB1_gcA&ccb=9-4&oh=00_AYHq4_mcwsfOxKM_tGhbB9j8du8yFa_RnRgQLIaJUWmZeQ&oe=67CFD425&_nc_sid=1d576d'
# import requests
# response = requests.get(url)
# with open("videooooo.mp4", "wb") as f:
#     f.write(response.content)
#
# # #----------------------------------
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
                model="gemini-2.0-flash",
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
                model="gemini-1.5-pro",
                # model="gemini-2.0-flash-lite-001",
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
# from IPython.display import Markdown

#---

# # Pass the video file reference like any other media part.
# response = client.models.generate_content(
#     model="gemini-1.5-pro",
#     contents=[
#         video_file,
#         "Summarize this video. Then create a quiz with answer key "
#         "based on the information in the video."])
#
# print(response)
 #---




# # Print the response, rendering any Markdown
# from IPython.display import Markdown
#
# # Print the response, rendering any Markdown
# Markdown(response.text)

# print('asdasd')
# Markdown(response.text)


# clientAI = googleAI()
#
# parsed_json = clientAI.GetAI_Image()
# base_parsed_json=parsed_json