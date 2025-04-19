from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)

# MongoDB Connection Setup
client = MongoClient('mongodb://45.149.76.168:13667')
db = client['Mohaddes_Project']
collection = db["Post_INFO_1404"]

@app.route('/search', methods=['POST'])
def search_posts():
    # Get query parameters from request and validate
    try:
        request_data = request.json
        if not request_data or not isinstance(request_data, dict):
            return jsonify({"error": "Invalid request format"}), 400
        
        # Extract query data
        test_data = request_data.get('data', [{}])[0]
        if not isinstance(test_data, dict):
            return jsonify({"error": "Invalid query format"}), 400
    except Exception as e:
        return jsonify({"error": f"Invalid request: {str(e)}"}), 400
    
    # Create MongoDB query
    query = {}
    for field, value in test_data.items():
        if not value:  # Skip empty values
            continue
            
        # Map field names to database field names
        db_field = field  # Default mapping
        if field == 'trueExploreMode':
            db_field = 'true_explore_mode'
        elif field == 'contentType':
            db_field = 'content_type'
        elif field == 'socialActivities':
            db_field = 'social_activities'
        elif field == 'contentVerification':
            db_field = 'content_verification'
        elif field == 'AgeRange':
            db_field = 'age_range'
        elif field == 'postTime':
            db_field = 'post_time'
        elif field == 'lifestylesPersonal':
            db_field = 'lifestyles_personal'
        
        # Add to query with improved matching
        if isinstance(value, list):
            if len(value) > 0:
                regex_conditions = []
                for v in value:
                    regex_conditions.append({db_field: {'$regex': f'.*{v}.*', '$options': 'i'}})
                if len(regex_conditions) == 1:
                    query.update(regex_conditions[0])
                else:
                    query['$or'] = regex_conditions
        else:
            if isinstance(value, str):
                query[db_field] = {'$regex': f'.*{value}.*', '$options': 'i'}
            else:
                query[db_field] = value

    # Execute MongoDB query
    results = list(collection.find(query))
    
    # Print results in command line
    print("\nQuery Parameters:")
    for key, value in query.items():
        print(f"{key}: {value}")

    result_count = 0
    print("\nFound Posts:")
    for result in results:
        result_count += 1
        print("\n" + "="*50)
        print(f"Post #{result_count}")
        print("-"*20)
        print(f"ID: {result.get('id', 'N/A')}")
        print(f"Caption: {result.get('caption_text', 'N/A')[:100]}...")
        print(f"Media Type: {result.get('media_type', 'N/A')}")
        print(f"Like Count: {result.get('like_count', 0):,}")
        print(f"Comment Count: {result.get('comment_count', 0):,}")
        print(f"View Count: {result.get('view_count', 0):,}")
        print(f"Play Count: {result.get('play_count', 0):,}")
        print(f"User: {result.get('user_username', 'N/A')} ({result.get('user_fullname', 'N/A')})")
        print(f"Posted: {result.get('created_at', 'N/A')}")
        
        print("\nContent Analysis:")
        print(f"Language: {result.get('languages', 'N/A')}")
        print(f"Emotions: {result.get('emotions', 'N/A')}")
        print(f"Audience: {result.get('audience', 'N/A')}")
        print(f"Topics: {', '.join(result.get('topics', ['N/A']))}")
        print(f"Sentiment: {', '.join(result.get('sentiment', ['N/A']))}")

    if result_count == 0:
        print("\nNo posts found matching the query criteria.")
    else:
        print(f"\nTotal posts found: {result_count}")

    # Return full documents as JSON response
    return json_util.dumps(results), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
                    