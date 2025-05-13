import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Access-Control-Allow-Origin': '*',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json',
    'Expires': '0',
    'Origin': 'http://185.221.237.210:3000',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://185.221.237.210:3000/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'name': '',
    'filters': {
        'contentType': [],
        'trueExploreMode': 'True Explore Mode',
        'credibility': [],
        'topics': [],
        'socialActivities': [],
        'languages': [],
        'emotions': [
            'Happy',
        ],
        'contentVerification': [],
        'audience': [],
        'source': [],
        'gender': [],
        'AgeRange': [],
        'postTime': [],
        'sensitivity': [],
        'sentiment': [],
        'lifestylesPersonal': [],
        'terends': [],
    },
}

response = requests.post('http://185.221.237.210:8765/search', headers=headers, json=json_data, verify=False)
