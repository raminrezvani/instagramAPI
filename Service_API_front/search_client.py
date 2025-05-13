import requests
import json

def search_posts(query_data):
    url = "http://185.221.237.210:8765/search"
    # url = "http://localhost:8765/search"
    headers = {"Content-Type": "application/json"}
    
    # Example query data structure
    data = {
        "data": [query_data]
    }
    
    # Make POST request to the API
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        # Parse and return the results
        results = json.loads(response.text)
        return results
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample query
    query = {
  "filters": {
    "contentType": [],
    "trueExploreMode": "True Explore Mode",
    "credibility": [],
    "topics": [],
    "socialActivities": [],
    "languages": [],
    "emotions": [],
    "contentVerification": [],
    "audience": [],
    "source": [],
    "gender": [
      "Male"
    ],
    "AgeRange": [],
    "postTime": [],
    "sensitivity": [],
    "sentiment": [],
    "lifestylesPersonal": [],
    "terends": []
  }
}
    
    # Execute search
    results = search_posts(query)
    
    # Print number of results
    if results:
        print(f"\nReceived {len(results)} results from API")
        
        # Optional: Print specific fields from results
        for i, post in enumerate(results, 1):
            print(f"\nPost {i}:")
            print(f"ID: {post.get('id')}")
            print(f"Caption: {post.get('caption_text', '')[:100]}...")
            print("-" * 50)