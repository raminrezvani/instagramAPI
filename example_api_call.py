import requests

# Base URL
base_url = "http://localhost:5000"

# # Example 1: Get all content analysis
# response = requests.get(f"{base_url}/api/content-analysis")
# print("All content:", response.json())

# Example 2: Get analysis for specific video
video_id = "video_1301647697784905v.mp4"
response = requests.get(f"{base_url}/api/content-analysis?video_id={video_id}")
print(f"Analysis for video {video_id}:", response.json())

# # Example 3: Get analysis from last week
# response = requests.get(f"{base_url}/api/content-analysis?time_range=week")
# print("Last week's analysis:", response.json())
#
# # Example 4: Combine filters
# response = requests.get(f"{base_url}/api/content-analysis?video_id={video_id}&time_range=month")
# print("Combined filters:", response.json())