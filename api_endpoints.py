from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)
api = None

class InstagramAPIEndpoints:
    def __init__(self):
        self.myclient = MongoClient('mongodb://45.149.76.168:13667')
        self.mydb = self.myclient["Mohaddes_Project"]
        self.mycol_ai_results = self.mydb["AI_Analysis_Results"]

    def init_routes(self):
        app.add_url_rule('/api/content-analysis', 'content_analysis', self.get_content_analysis, methods=['GET'])

    def get_content_analysis(self):
        try:
            # Get query parameters
            video_id = request.args.get('video_id')
            time_range = request.args.get('time_range', 'all')  # all, today, week, month
            
            # Build query
            query = {}
            if video_id:
                query['video_id'] = video_id
            
            if time_range != 'all':
                time_filters = {
                    'today': datetime.now() - timedelta(days=1),
                    'week': datetime.now() - timedelta(weeks=1),
                    'month': datetime.now() - timedelta(days=30)
                }
                if time_range in time_filters:
                    query['analysis_date'] = {'$gte': time_filters[time_range]}
            
            # Get results from MongoDB
            results = list(self.mycol_ai_results.find(query, {'_id': 0}))
            
            # Format response
            response = {
                'status': 'success',
                'count': len(results),
                'data': [{
                    'trueExploreMode': result.get('true_explore_mode'),
                    'contentType': result.get('content_type', []),
                    'credibility': result.get('credibility', []),
                    'topics': result.get('topics', []),
                    'socialActivities': result.get('social_activities', []),
                    'languages': result.get('languages', []),
                    'emotions': result.get('emotions', []),
                    'contentVerification': result.get('content_verification', []),
                    'audience': result.get('audience', []),
                    'source': result.get('source', []),
                    'gender': result.get('gender', []),
                    'AgeRange': result.get('age_range', []),
                    'postTime': result.get('post_time', []),
                    'sensitivity': result.get('sensitivity', []),
                    'sentiment': result.get('sentiment', []),
                    'lifestylesPersonal': result.get('lifestyles_personal', []),
                    'trends': result.get('trends', [])
                } for result in results]
            }
            
            return jsonify(response)
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

def create_app():
    global api
    api = InstagramAPIEndpoints()
    api.init_routes()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)